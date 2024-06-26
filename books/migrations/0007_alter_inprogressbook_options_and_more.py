# Generated by Django 4.2.6 on 2023-11-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0006_remove_book_waiting_timer"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="inprogressbook",
            options={"verbose_name": "In Progress Book"},
        ),
        migrations.AlterField(
            model_name="inprogressbook",
            name="pages_left",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Pages Left"
            ),
        ),
    ]
