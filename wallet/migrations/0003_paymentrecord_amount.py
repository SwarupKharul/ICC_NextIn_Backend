# Generated by Django 4.1.7 on 2023-02-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wallet", "0002_rename_ticket_payment_record_no_of_tickets_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="paymentrecord",
            name="amount",
            field=models.BigIntegerField(default=0),
        ),
    ]