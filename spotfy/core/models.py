from django.db import models

class Playlist(models.Model):

    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = u'Playlist'
        verbose_name_plural = u'Playlist'
        
    def __str__(self):
        return self.name
