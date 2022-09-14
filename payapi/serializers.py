from rest_framework import serializers
from .models import Merchant, Account, Transaction, Transfer


class PaySerializer(serializers.Serializer):

    type = serializers.CharField(max_length=16)
    merchant_id = serializers.IntegerField()
    transaction_id = serializers.CharField(max_length=16)
    merchant_name = serializers.CharField(max_length=255)
    merchant_mcc = serializers.IntegerField()
    billing_amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    billing_currency = serializers.CharField(max_length=3)
    transaction_amount = serializers.DecimalField(max_digits=11, decimal_places=2)
    transaction_currency = serializers.CharField(max_length=3)
    settlement_amount = serializers.DecimalField(max_digits=11, decimal_places=2, required=False)
    settlement_currency = serializers.CharField(max_length=3, required=False)


class TransactionsSerializer(serializers.Serializer):

    merchant_id = serializers.IntegerField()
    # start_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    # end_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')


class BalancesSerializer(serializers.Serializer):

    merchant_id = serializers.IntegerField()
    type = serializers.CharField(max_length=9)
