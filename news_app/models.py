from django.db import models
from django.db.models import TextField
from django.urls import reverse
from django.utils import timezone

from django.core.validators import FileExtensionValidator
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)




class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Advertisement(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        Published = 'PB', "Published"

    title = models.CharField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Published)
    objects = models.Manager()
    published = PublishedManager()




class News(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DR', 'Draft'
        Published = 'PB', "Published"
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='news/images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now= True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    objects = models.Manager()
    published =PublishedManager()

    class Meta:
        ordering = ["-publish_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail_page", args= [self.slug])



class FooterData(models.Model):
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    site_created = TextField()

    def __str__(self):
        return self.phone

class FormModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class MyModel(models.Model):
    video = models.FileField(
        upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])]
    )

    def __str__(self):
        return self.video












