# Generated by Django 4.1.2 on 2023-03-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_alter_order_order_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_number",
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
