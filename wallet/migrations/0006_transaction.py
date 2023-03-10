# Generated by Django 4.1.7 on 2023-03-01 22:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wallet.models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wallet", "0005_paymentrecord_timestamp"),
    ]

    operations = [
        migrations.CreateModel(
            name="transaction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "transaction_hash",
                    models.CharField(
                        default=wallet.models.generate_hash_id, max_length=36
                    ),
                ),
                ("amount", models.BigIntegerField(default=0)),
                ("timestamp", models.DateTimeField(auto_now_add=True, null=True)),
                ("note", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "buyer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
