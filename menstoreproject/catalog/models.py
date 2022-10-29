from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    description = models.TextField(blank=True, verbose_name='Опис категорії')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Назва товару')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорія')
    description = models.TextField(blank=True, verbose_name='Опис товару')
    price = models.IntegerField()
    material = models.CharField(max_length=50, verbose_name='Матеріал')
    quantity = models.IntegerField()
    item_code = models.IntegerField(verbose_name='Код товару')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['name']


class ProductImage(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    product = models.ForeignKey('Product', on_delete=models.PROTECT,)