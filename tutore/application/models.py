from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self) :
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self) :
        return self.name


class Files(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    sub_category = models.ForeignKey(SubCategory, related_name='categorie', on_delete=models.CASCADE)
    Auteur = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=200)
    date_de_modification = models.DateField(blank=True, null=True)
    dernier_contributeur = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self) :
        return self.title