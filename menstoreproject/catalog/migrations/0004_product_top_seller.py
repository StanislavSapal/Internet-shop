# Generated by Django 4.1.2 on 2023-01-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_merge_0002_alter_category_slug_0002_product_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="top_seller",
            field=models.BooleanField(default=False, verbose_name="Топ продажів"),
        ),
    ]