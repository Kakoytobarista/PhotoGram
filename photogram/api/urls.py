from django.urls import include, path
from rest_framework import routers

from api.views import PhotoViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('photo', PhotoViewSet, basename='photos')


urlpatterns = (
    path('', include(router.urls)),
)
