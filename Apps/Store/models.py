from itertools import product
from pyexpat import model
from unicodedata import category, decimal
from django.db import models
from Users.models import BaseModels
from smart_selects.db_fields import ChainedForeignKey

class Category(BaseModels):
    descreption = models.CharField("Descreption of category", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural="Categorys"
        ordering = ['name']
        app_label = 'Store'
    
    def __str__(self):
        return self.name

class SubCategory(BaseModels):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category_of_the_subcategory")
    descreption = models.CharField("Descreption of SubCategory", max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural="SubCategorys"
        ordering = ['name']
        app_label = 'Store'

    def __str__(self):
        return self.name

class Product(BaseModels):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category_of_the_subcategory_product")
    city = ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True
        )  
    price = models.FloatField("Price of the product", max_digits=5, decimal_places=2)
    warranty = models.CharField("Warranty of the product", max_length=14)
    profile_picture = models.ImageField("Foto de Perfil",  null=True, blank=True, upload_to="FotodePerfilPorduct/")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural="Product"
        ordering = ['name']
        app_label = 'Store'

    def __str__(self):
        return self.name

class PhotoGallery(BaseModels):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="photo_gallery_of_the_product")

    class Meta:
        verbose_name = "Photo Gallery"
        verbose_name_plural="Photos Gallery"
        ordering = ['name']
        app_label = 'Store'

    def __str__(self):
        return self.name

class Photo(models.Model):
    photo_gallery = models.ForeignKey("PhotoGallery", related_name="photo_of_the_gallery", on_delete = models.CASCADE)
    photo = models.ImageField(verbose_name = 'Imagens da galeria de foto', upload_to = "imagens-da-galeria")

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photo"
        ordering = ['photo_gallery']
        app_label = "Store"

    def __str__(self):
        return str(self.photo_gallery)

class Specifications(BaseModels):
    product = models.ForeignKey("Product", related_name="specifications_of_the_product", on_delete = models.CASCADE)
   
    class Meta:
        verbose_name = "Specification"
        verbose_name_plural = "Specifications"
        ordering = ['product']
        app_label = "Store"

    # def __str__(self):
    #     return "Questionario do pacote " + str(self.pacote)

class Descreption(BaseModels):
   
    class Meta:
        verbose_name = "Descreption"
        verbose_name_plural = "Descreptions"
        ordering = ['name']
        app_label = "Store"

    def __str__(self):
        return str(self.name)

class Answer(BaseModels):
    descreption = models.ForeignKey("Descreption", on_delete = models.CASCADE, related_name="answer_of_the_descreption")
    

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"
        ordering = ['name']
        app_label = "Store"

    def __str__(self):
        return str(self.name)




