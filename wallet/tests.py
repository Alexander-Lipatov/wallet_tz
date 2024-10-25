import uuid
from django.test import TestCase
from django.urls import reverse
from .models import Wallet
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.response import Response
# Create your tests here.


class WalletTestCase(TestCase):
    def setUp(self):
        self.uuid = uuid.uuid4()
        self.client = APIClient()

        self.wallet = Wallet.objects.create(name="wallet_1", uuid=self.uuid, balance=1000)

        self.get_wallet_url = reverse('wallet', kwargs={'uuid_wallet': str(self.wallet.uuid)})
        self.operation_url = reverse('wallet_operation', kwargs={'uuid': str(self.wallet.uuid)})


    def test_get_wallet_success(self):
        """Проверка успешного получения кошелька."""

        response:Response = self.client.get(self.get_wallet_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['uuid'], str(self.wallet.uuid))
        self.assertEqual(float(response.data['balance']), float(self.wallet.balance))

    def test_get_wallet_invalid_uuid(self):
        """Проверка ответа при передаче неверного UUID."""

        response:Response = self.client.get(reverse('wallet', kwargs={'uuid_wallet': 'invalid-uuid'}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Invalid UUID.')
    
    def test_get_wallet_not_found(self):
        """Проверка ответа, когда кошелек не найден."""

        response:Response = self.client.get(reverse('wallet', kwargs={'uuid_wallet': str(uuid.uuid4())}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Wallet not found.')


    def test_wallet_operation_deposit(self):
        """Проверка успешного пополнения кошелька."""

        data = {
            'operation_type': 'DEPOSIT',
            'amount': 500
        }
        response:Response = self.client.post(self.operation_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(float(self.wallet.balance), float(1500))

    def test_wallet_operation_withdraw(self):
        """Проверка успешного списания средств с кошелька."""

        data = {
            'operation_type': 'WITHDRAW',
            'amount': 500
        } 
        response = self.client.post(self.operation_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wallet.refresh_from_db()
        self.assertEqual(float(self.wallet.balance), float(500))

    def test_wallet_operation_invalid_data(self):
        """Проверка обработки неверных данных для операции."""

        data = {
            'operationType': 'INVALID_OPERATION',
            'amount': 500
        }
        response:Response = self.client.post(self.operation_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('operation_type', response.data['detail'])

        