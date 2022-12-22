
from django.db import models



#  Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    branches=models.CharField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    available_loans=models.CharField(max_length=250,unique=True)
    Internet_banking=models.BooleanField(default=True)


    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return '{}'.format(self.name)

class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    branches = models.CharField(max_length=250, unique=True)
    desc = models.TextField(blank=True)
    contact_number=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)


    class Meta:
        ordering=('name',)
        verbose_name='district'
        verbose_name_plural='districts'

    def __str__(self):
        return '{}'.format(self.name)






