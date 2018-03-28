from rest_framework import generics
from .models import Music, Record, Band, Playlist
from .serializers import MusicSerializer, RecordSerializer, BandSerializer, PlayListSerializer

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_condition import Or
from django_filters import rest_framework as filters



# Create your views here.
class MusicList(generics.ListCreateAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class RecordList(generics.ListCreateAPIView):

    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class BandList(generics.ListCreateAPIView):

    queryset = Band.objects.all()
    serializer_class = BandSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class BandDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class PlayListFilter(filters.FilterSet):

    year_a = filters.DateFilter(name="year", lookup_expr='a')
    year_b = filters.DateFilter(name="year", lookup_expr='b')

    class Meta:
        model = Playlist
        fields = '__all__'

class PlayList(generics.ListCreateAPIView):

    queryset = Playlist.objects.all()
    serializer_class = PlayListSerializer    
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)    
    filter_class = PlayListFilter  

class PlayListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlayListSerializer                       
    #authentication_classes = [SessionAuthentication]
    #permission_classes = (IsAuthenticated, )
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
