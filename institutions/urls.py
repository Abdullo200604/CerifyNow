from django.urls import path
from .views import (
    InstitutionListCreateAPIView,
    CertificateListCreateAPIView,
    CertificateDetailAPIView
)

urlpatterns = [
    path('institutions/', InstitutionListCreateAPIView.as_view(), name='institution-list-create'),
    path('certificates/', CertificateListCreateAPIView.as_view(), name='certificate-list-create'),
    path('certificates/<uuid:pk>/', CertificateDetailAPIView.as_view(), name='certificate-detail'),
]
