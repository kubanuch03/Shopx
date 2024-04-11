# Generated by Django 5.0.4 on 2024-04-11 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(blank=True, max_length=200, unique=True)),
                ("img", models.ImageField(blank=True, upload_to="products/%Y/%m/%d")),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ["name"],
                "indexes": [
                    models.Index(fields=["name"], name="Category_ca_name_9c6f4f_idx")
                ],
            },
        ),
        migrations.CreateModel(
            name="PodCategory",
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
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="PodCategory",
                        to="Category.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "podcategory",
                "verbose_name_plural": "podcategory",
                "ordering": ["name"],
                "indexes": [
                    models.Index(fields=["name"], name="Category_po_name_8266ff_idx")
                ],
            },
        ),
    ]
