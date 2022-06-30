from distutils.command.upload import upload
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import random

from requests import request


# Create your models here.

class ProductBase(models.Model):
    title = models.CharField(
        max_length=200, verbose_name="Tytuł", null=False, blank=False)
    text = models.TextField(verbose_name="Opis", null=False, blank=False)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, verbose_name="Cena", null=False, blank=False)
    from_state = models.CharField(
        max_length=100, verbose_name="Województwo", null=False, blank=False)
    from_city = models.CharField(
        max_length=100, verbose_name="Miasto", null=False, blank=False)
    publication_time = models.DateTimeField(
        null=False, blank=False, auto_now_add=True)
    # author = models.OneToOneField(User, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL)
    slug = models.SlugField(blank=True, null=True)
    category = models.ForeignKey(
        'CategoryClass', null=True, blank=True, on_delete=models.SET_NULL)
    thumb = models.ImageField(upload_to="media/", blank=True, null=True)
    brand = models.ForeignKey(
        'Brand', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Produkt Bazowy"
        verbose_name_plural = "Produkty bazowe"

    # def save_model(self, request, obj, form, change):
    #     self.author_id = request.user
    #     super().save_model(request, obj, form, change)

    # def save(self, *args, **kwargs):
    #     self.author_id = request.user
    #     super(ProductBase, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        time = timezone.now()
        minutes = time.minute
        seconds = time.second
        rand = random.randint(10000, 5010000)

        if not self.slug:
            self.slug = slugify(self.title)
            self.slug += str(minutes) + str(seconds) + str(rand)

        super(ProductBase, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

# --------------------------------------------------------


class CategoryClass(models.Model):
    category_name = models.CharField(max_length=50, blank=True)
    category_image = models.ImageField(upload_to="category/", blank=True)
    category_slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


# --------------------------------------------------------

class ProductImages(models.Model):
    product = models.ForeignKey(ProductBase, on_delete=models.CASCADE)
    image01 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image02 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image03 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image04 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image05 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image06 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image07 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image08 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image09 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)
    image10 = models.ImageField(
        upload_to="products_images/", blank=True, null=True)

    class Meta:
        verbose_name = "Zdjęcia produktu"
        verbose_name_plural = "Zdjęcia produktów"

    def __str__(self):
        return self.product.title

# --------------------------------------------------------


class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Marka produktu"
        verbose_name_plural = "Marka produktów"

    def __str__(self):
        return self.brand_name
