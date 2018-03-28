from rest_framework import serializers
from .models import Record, Genre, Band, Music, Playlist

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        
        
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
        
class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'
        
        
class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'
        
        
class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'