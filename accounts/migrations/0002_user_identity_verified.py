# Generated by Django 4.2.6 on 2023-11-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="identity_verified",
            field=models.BooleanField(default=False),
        ),
    ]
