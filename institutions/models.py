import uuid
import hashlib
from django.db import models
from users.models import User

def get_file_hash(file_field):
    hasher = hashlib.sha256()
    for chunk in file_field.chunks():
        hasher.update(chunk)
    return hasher.hexdigest()

class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    inn = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    seal = models.ImageField(upload_to='institution_seals/', blank=True, null=True)
    logo = models.ImageField(upload_to='institution_logos/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='institutions',
        limit_choices_to={'role': 'institution_admin'}
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='certificates')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates', limit_choices_to={'role': 'student'})
    file = models.FileField(upload_to='certificates/')
    hash = models.CharField(max_length=128, unique=True, blank=True)
    qr_code = models.ImageField(upload_to='certificate_qrcodes/', blank=True, null=True)
    document_type = models.CharField(max_length=50)
    issued_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.file and not self.hash:
            self.file.seek(0)
            self.hash = get_file_hash(self.file)
            self.file.seek(0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.document_type} — {self.student.get_full_name()} — {self.institution.name}"
