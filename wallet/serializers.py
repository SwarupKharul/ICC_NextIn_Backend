from rest_framework import serializers

from .models import paymentRecord, transaction
from match.serializers import MatchSerializer


class PaymentRecordSerializer(serializers.ModelSerializer):
    match = MatchSerializer()

    class Meta:
        model = paymentRecord
        fields = (
            "user",
            "razorpay_order_id",
            "razorpay_payment_id",
            "razorpay_signature",
            "status",
            "tier",
            "no_of_tickets",
            "amount",
            "match",
            "timestamp",
        )


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = (
            "buyer",
            "seller",
            "amount",
            "note",
        )

class GetTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = (
            "buyer",
            "transaction_hash",
            "seller",
            "amount",
            "timestamp",
            "note",
        )
