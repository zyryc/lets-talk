from django.contrib import admin
from django.urls import include, path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('miniblog.urls')),
    path('admin/', admin.site.urls),
    path('miniblog/', include('django.contrib.auth.urls')),
]
# required to see the media files in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

