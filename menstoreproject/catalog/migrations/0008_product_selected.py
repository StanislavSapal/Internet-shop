# Generated by Django 4.1.2 on 2023-04-10 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_size"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="selected",
            field=models.BooleanField(default=False, verbose_name="На банері"),
        ),
    ]
