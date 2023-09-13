from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    slug = models.SlugField(unique=True)        #'My Awesome Article' sets to 'my-awesome-article'
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name


class Book(models.Model):

    title =	models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.title}: {self.author}'
    class Meta:
        indexes = [models.Index(fields=['price']),]

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id =  models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    rating = models.SmallIntegerField()