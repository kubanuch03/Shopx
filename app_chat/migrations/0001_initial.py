# Generated by Django 5.0.3 on 2024-03-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField()),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("date_added",),
            },
        ),
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(unique=True)),
                ("is_deleted_user1", models.BooleanField(default=False)),
                ("is_deleted_user2", models.BooleanField(default=False)),
            ],
        ),
    ]
