
# Generated by Django 4.2.11 on 2024-03-21 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user_profiles", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Category", "0001_initial"),
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recall",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="Category.category",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="podcategory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pod_products",
                to="Category.podcategory",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="user",
            field=models.ForeignKey(
                limit_choices_to={"is_seller": True},
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="user_profiles.sellerprofile",
            ),
        ),
        migrations.AddField(
            model_name="like",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="product.product"
            ),
        ),
        migrations.AddField(
            model_name="like",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["id", "slug"], name="product_pro_id_b9e5a0_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["name"], name="product_pro_name_b60cd1_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(
                fields=["-created"], name="product_pro_created_942044_idx"
            ),
        ),
    ]
