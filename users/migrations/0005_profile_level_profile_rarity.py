# Generated by Django 4.1.7 on 2023-03-01 17:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_profile_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="level",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="profile",
            name="rarity",
            field=models.IntegerField(default=0),
        ),
    ]
