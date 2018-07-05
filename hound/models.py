#Models for the PodHound app
from django.db import models
from django.core.validators import URLValidator

class Publisher(models.Model):
    publisher_name = models.CharField()
    description = models.TextField()
    website = models.TextField(validators=[URLValidator()])
    artwork = models.ImageField(upload_to = 'images/publishers', default = 'images/none/no-img.jpg')
    shows = models.ForeignKey(Show)

class Show(models.Model):
    show_name = models.CharField()
    show_description = models.TextField()pic_folder
    artwork = models.ImageField(upload_to = 'images/episodes', default = 'images/none/no-img.jpg')
    start_date = models.DateField()
    last_update = models.DateField()
    rating = models.IntegerField()
    feed_url = models.TextField(validators=[URLValidator()])
    episodes =  models.ManyToManyField(Episode)
    publisher = ForeignKey(Publisher)

class Episode(models.Model):
    title = models.CharField()
    summary = models.TextField()
    publish_date = models.DateField()
    listened = models.BooleanField()
    show = models.ForeignKey(Show)
