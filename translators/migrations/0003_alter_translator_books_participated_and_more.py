# Generated by Django 4.2.6 on 2023-11-15 13:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("translators", "0002_alter_translator_books_participated_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="translator",
            name="books_participated",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="translator",
            name="pages_translated",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="translator",
            name="translation_accuracy",
            field=models.PositiveIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(100)]
            ),
        ),
    ]
