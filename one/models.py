from django.db import models

# Create your models here.

class List(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Card(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    list=models.ForeignKey(List,related_name='cards',default='')
    story_points=models.IntegerField(null=True,blank=True)
    bussiness_values=models.IntegerField(null=True,blank=True)

    def __str__(self):

        return self.title
