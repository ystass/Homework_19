# Generated by Django 5.0.6 on 2024-06-17 12:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_in_stock"),
    ]

    operations = [
        migrations.CreateModel(
            name="Version",
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
                ("version_number", models.IntegerField(verbose_name="номер версии")),
                ("name", models.CharField(verbose_name="название версии")),
                ("is_active", models.BooleanField(verbose_name="активная версия")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="prod",
                        to="catalog.product",
                        verbose_name="продукт",
                    ),
                ),
            ],
            options={
                "verbose_name": "версия",
                "verbose_name_plural": "версии",
            },
        ),
    ]
