from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.urls import reverse
import random
import json

import datetime
from django.utils import timezone

class World(models.Model):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    food_distribution = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    life_distribution = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    data = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('world-detail', kwargs={"slug": self.alias})

    def get_lifeform(self):
        return self.lifeform_set.filter(x=self.x, y=self.y)

class LifeForm(models.Model):
    mother = models.ForeignKey('self', related_name='related_mother', null=True)
    father = models.ForeignKey('self', related_name='related_father', null=True)
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=1)
    health = models.IntegerField(default=100, validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField(default=True)

class Plot(models.Model):
    world = models.ForeignKey(World, on_delete=models.CASCADE)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    feature = models.CharField(max_length=10, null=True)

@receiver(pre_save, sender=World)
def save_alias(sender, instance, *args, **kwargs):
    if not instance.alias:
        instance.alias = slugify(instance.name) + '-' + str(random.randrange(1000, 9999))

    data = [[0 for x in range(instance.width)] for y in range(instance.height)]
    LifeForm.objects.filter(world=instance).delete()
    for x in range(instance.width):
        for y in range(instance.height):
            if random.randrange(1, 100) <= instance.food_distribution:
                data[y][x] = 'food'
            elif random.randrange(1, 100) <= instance.life_distribution:
                life_form = LifeForm(world=instance, x=x, y=y)
                if random.randrange(1, 100) <= 50:
                    data[y][x] = 'lifeform male'
                    life_form.sex = 'm'
                else:
                    data[y][x] = 'lifeform female'
                    life_form.sex = 'f'
                life_form.save()

    instance.data = json.dumps(data)
