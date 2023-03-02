from django.contrib import admin
from .models import paymentRecord, transaction

admin.site.register(paymentRecord)
admin.site.register(transaction)
