# Generated by Django 4.1.2 on 2022-10-31 16:52

from django.db import migrations, models
import django.db.models.deletion


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
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=150, verbose_name="Назва категорії"
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Фото"
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Опис категорії"),
                ),
            ],
            options={
                "verbose_name": "Категорія",
                "verbose_name_plural": "Категорії",
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=150, verbose_name="Назва товару")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Опис товару"),
                ),
                ("price", models.IntegerField()),
                ("material", models.CharField(max_length=50, verbose_name="Матеріал")),
                ("quantity", models.IntegerField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="catalog.category",
                        verbose_name="Категорія",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товари",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                (
                    "image",
                    models.ImageField(
                        blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Фото"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.product",
                    ),
                ),
            ],
        ),
    ]
