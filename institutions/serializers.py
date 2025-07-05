from rest_framework import serializers
from users.models import User
from .models import Institution, Certificate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number', 'profile_photo']

class InstitutionSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)
    class Meta:
        model = Institution
        fields = [
            'id', 'name', 'inn', 'address', 'phone', 'email', 'seal',
            'logo', 'website', 'is_approved', 'admin', 'created_at'
        ]

class CertificateSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer(read_only=True)
    student = UserSerializer(read_only=True)
    class Meta:
        model = Certificate
        fields = [
            'id', 'institution', 'student', 'file', 'hash', 'qr_code',
            'document_type', 'issued_date', 'description', 'is_verified', 'created_at'
        ]
