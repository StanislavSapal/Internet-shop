# Generated by Django 4.1.2 on 2022-12-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
