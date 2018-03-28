from django.contrib import admin
from django.conf.urls import url,include


urlpatterns = [

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    url(r'^', include('core.urls')),
    url(r'^playlist/', include('playlist.urls')),
    url(r'^admin/', admin.site.urls),
]
