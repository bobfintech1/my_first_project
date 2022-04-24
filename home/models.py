from uuid import uuid4

from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'news_archive/{filename}'.format(
        filename='{}.{}'.format(uuid4().hex, ext)
    )
    return file_path


class HomeModel(models.Model):
    title = models.CharField(max_length=15)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    data = models.DateField('Date', default=date.today)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('home:detail', args=[str(self.id)])

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url


class HomeArticleModel(models.Model):
    title = models.CharField(max_length=15)
    body = models.TextField()
    data = models.DateField('Date', default=date.today)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)
