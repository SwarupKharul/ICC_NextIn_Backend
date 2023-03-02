import uuid
from django.db import models
from django.contrib.auth import get_user_model
from match.models import Match
from django.utils.crypto import get_random_string

User = get_user_model()


def generate_hash_id():
    unique_id = uuid.uuid4()
    unique_id = str(unique_id).replace("-", "")
    unique_id = "0x" + unique_id
    return unique_id


class paymentRecord(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=100)
    razorpay_payment_id = models.CharField(max_length=100)
    razorpay_signature = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    tier = models.CharField(default="no", max_length=50)
    no_of_tickets = models.IntegerField(default=1)
    amount = models.BigIntegerField(default=0)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.email


class transaction(models.Model):
    objects = None
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_hash = models.CharField(
        max_length=36, default=generate_hash_id, editable=False
    )
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    amount = models.BigIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    note = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.transaction_hash
