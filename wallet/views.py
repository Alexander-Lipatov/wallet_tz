import uuid

from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Wallet
from .serializers import WalletSerializer,WalletOperationsSerializer

class WalletOperationView(APIView):

    @transaction.atomic
    def post(self, request: Request, uuid):
        wallet = get_object_or_404(Wallet.objects.select_for_update(), uuid=uuid)
        serializer = WalletOperationsSerializer(data=request.data, context={'wallet':wallet})
        if serializer.is_valid():
            wallet = serializer.update_balance()
            return Response({'wallet_uuid': wallet.uuid, 'balance': wallet.balance}, status=status.HTTP_200_OK)
        return Response({ 'detail':serializer.errors},status=status.HTTP_400_BAD_REQUEST,)
    

class GetWalletView(APIView):

    def get(self, request:Request, uuid_wallet):
        try:
            wallet = Wallet.objects.get(uuid=uuid.UUID(uuid_wallet))
        except ValueError:
            return Response({'detail': 'Invalid UUID.'}, status=status.HTTP_400_BAD_REQUEST)
        except Wallet.DoesNotExist:
            return Response({'detail': 'Wallet not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WalletSerializer(wallet)
        return Response(serializer.data)