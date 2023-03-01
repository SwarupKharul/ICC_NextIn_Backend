from rest_framework import serializers

from .models import paymentRecord
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
            "match",
        )
