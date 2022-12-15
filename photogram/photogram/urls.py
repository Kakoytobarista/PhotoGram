from django.urls import include, path

from photogram import settings

from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = [
    path('', include('photo.urls', namespace='photo')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
