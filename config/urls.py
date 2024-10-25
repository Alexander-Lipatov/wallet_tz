
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/wallets/', include('wallet.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
