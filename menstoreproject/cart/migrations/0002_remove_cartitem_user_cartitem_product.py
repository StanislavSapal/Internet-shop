# Generated by Django 4.1.2 on 2023-01-18 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_merge_0002_alter_category_slug_0002_product_slug"),
        ("cart", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="cartitem", name="user",),
        migrations.AddField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="catalog.product",
            ),
        ),
    ]
