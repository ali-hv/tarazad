# Generated by Django 4.2.6 on 2023-11-03 19:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0012_inprogressbook_is_done"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inprogressbook",
            name="is_done",
        ),
    ]
