from rest_framework import generics, permissions
from .models import Institution, Certificate
from .serializers import InstitutionSerializer, CertificateSerializer

# Institution ro‘yxati va yaratish
class InstitutionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Certificate (hujjat) ro‘yxati va yaratish (upload)
class CertificateListCreateAPIView(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Certificate detail view (bitta hujjat uchun)
class CertificateDetailAPIView(generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.AllowAny]
