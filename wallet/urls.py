
from django.urls import path

from .views import WalletOperationView, GetWalletView

urlpatterns = [
    path('<uuid:uuid>/operation', WalletOperationView.as_view(), name='wallet_operation'),
    path('<str:uuid_wallet>', GetWalletView.as_view(), name='wallet')
]
