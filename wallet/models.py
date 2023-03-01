from django.db import models
from django.contrib.auth import get_user_model
from match.models import Match

User = get_user_model()


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

    def __str__(self):
        return self.user.email
