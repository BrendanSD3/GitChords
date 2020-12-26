from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField('Song Name', max_length=120)
    artist = models.CharField('Artist', max_length=120)
    
    Chords = (
        ('A', 'A Chord'),
        ('G', 'G Chord'),
        ('D', 'D chord'),
        ('C', 'C chord'),
        ('F', 'F chord'),
    )
    chords = models.CharField(max_length=1, choices=Chords)
    
    def __str__(self):
        return self.name

