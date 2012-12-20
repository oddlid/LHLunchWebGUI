#from django.db import models
#
## Create your models here.
#
#class Restaurant(models.Model):
#   name = models.CharField('restaurant name', max_length=128)
#   src_url = models.URLField('source url', max_length=255)
#   parsed = models.DateTimeField('date parsed')
#
#   def __init__(self, name, url, parsed):
#      self.name = name
#      self.src_url = url
#      self.parsed = parsed
#
#   def __unicode__(self):
#      return self.name
#
#class Dish(models.Model):
#   restaurant = models.ForeignKey(Restaurant)
#   name = models.CharField('dish name', max_length=128)
#   price = models.IntegerField('dish price')
#   desc = models.TextField('dish description')
#
#   def __init__(self, restaurant, name, price, desc):
#      self.restaurant = restaurant
#      self.name = name
#      self.price = price
#      self.desc = desc
#
#   def __unicode__(self):
#      return self.name
