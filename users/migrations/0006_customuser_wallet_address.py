# Generated by Django 4.1.7 on 2023-03-02 00:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_profile_level_profile_rarity"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="wallet_address",
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
