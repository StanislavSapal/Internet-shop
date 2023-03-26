# Generated by Django 4.1.2 on 2023-03-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_productsize_alter_productimage_options_product_size"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productsize",
            options={
                "ordering": ["id"],
                "verbose_name": "Розмір товару",
                "verbose_name_plural": "Розміри товарів",
            },
        ),
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.ManyToManyField(
                to="catalog.productsize", verbose_name="Розмір"
            ),
        ),
    ]
