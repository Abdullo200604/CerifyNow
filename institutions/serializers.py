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
    qr_code_url = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = [
            'id', 'institution', 'student', 'file', 'hash', 'qr_code', 'qr_code_url',
            'document_type', 'issued_date', 'description', 'is_verified', 'created_at'
        ]

    def get_qr_code_url(self, obj):
        if obj.qr_code and hasattr(obj.qr_code, 'url'):
            return obj.qr_code.url
        return None
