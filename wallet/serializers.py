from decimal import Decimal
from rest_framework import serializers
from .models import Wallet
from django.utils.functional import lazy
from django.db.models import F


class WalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ['id', 'name', 'balance', 'uuid']


class WalletOperationsSerializer(serializers.Serializer):

    OPERATION_CHOICE = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
    )
    operation_type = serializers.ChoiceField(OPERATION_CHOICE)
    amount = serializers.DecimalField(
        max_digits=10, decimal_places=2, min_value=Decimal('0.01'))

    def validate(self, attrs):
        wallet: Wallet = self.context['wallet']

        if attrs['operation_type'] == 'WITHDRAW' and wallet.balance < attrs['amount']:
            raise serializers.ValidationError(
                'Не достаточно средств для выполнения операции')

        return attrs

    def update_balance(self):
        wallet:Wallet = self.context['wallet']
        operation_type = self.validated_data['operation_type']
        amount = self.validated_data['amount']

        if operation_type == 'DEPOSIT':
            wallet.balance = F('balance') + amount
        else:
            wallet.balance = F('balance') - amount

        wallet.save(update_fields=['balance'])
        wallet.refresh_from_db() 
        return wallet
