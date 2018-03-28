from __future__ import unicode_literals
from django.db import models


class Record(models.Model):

    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = u'Record'
        verbose_name_plural = u'Records'
        
    def __str__(self):
        return self.name
  
  
class Genre(models.Model):

    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = u'Genre'
        verbose_name_plural = u'Genres'
        
    def __str__(self):
        return self.name
      
      
class Band(models.Model):

    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, verbose_name="Genre", on_delete=models.CASCADE)
    record = models.ForeignKey(Record, verbose_name='Record', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Band'
        verbose_name_plural = u'Bands'
        
    def __str__(self):
        return self.name
      
      
class Music(models.Model):

    name = models.CharField(max_length=100)
    band = models.ForeignKey(Band, verbose_name="Band", on_delete=models.CASCADE)
    duration = models.TimeField()
    year = models.DateField()
   
    class Meta:
        verbose_name = u'Music'
        verbose_name_plural = u'Musics'
        
    def __str__(self):
        return self.name
      
      
class Playlist(models.Model):

    name = models.CharField(max_length=100)
    music = models.ManyToManyField(Music, verbose_name='Music')

    class Meta:
        verbose_name = u'Playlist'
        verbose_name_plural = u'Playlists'

    def __str__(self):
        return self.name