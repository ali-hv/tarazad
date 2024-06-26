# Generated by Django 4.2.6 on 2023-11-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0013_remove_inprogressbook_is_done"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="file",
            new_name="original_file",
        ),
        migrations.AddField(
            model_name="book",
            name="translated_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="books/translated/",
                verbose_name="Book's Translated File",
            ),
        ),
    ]
