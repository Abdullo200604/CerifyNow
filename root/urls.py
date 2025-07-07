from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('institutions.urls')),  # yoki api/ orqali institutions-urls chaqirilgan bo'ladi
]
