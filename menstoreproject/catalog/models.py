from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Назва категорії')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True,)
    description = models.TextField(blank=True, verbose_name='Опис категорії')

    def get_absolute_url(self):
        return reverse('products_by_category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['title']


class ProductSize(models.Model):
    size = models.CharField(max_length=5, verbose_name='Розмір')

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'Розмір товару'
        verbose_name_plural = 'Розміри товарів'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Назва товару')
    slug = models.SlugField(unique=True, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категорія')
    description = models.TextField(blank=True, verbose_name='Опис товару')
    price = models.IntegerField()
    material = models.CharField(max_length=50, verbose_name='Матеріал')
    quantity = models.IntegerField()
    top_seller = models.BooleanField(default=False, verbose_name='Топ продажів')
    size = models.ManyToManyField(ProductSize, blank=True, verbose_name="Розмір")
    selected = models.BooleanField(default=False, verbose_name='На банері')

    def get_absolute_url(self):
        return reverse('view_product', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['name']


class ProductImage(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Головна')

    def get_absolute_url(self):
        return reverse('view_product', kwargs={'pk': self.pk})

    def get_img(self):
        return self.image

    class Meta:
        verbose_name = 'Фото товару'
        verbose_name_plural = 'Фото товарів'
