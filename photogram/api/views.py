from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.serializers import GetPhotoSerializer
from photo.models import Photo


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.select_related('photo').all()
    serializer_class = GetPhotoSerializer
    permission_classes = (AllowAny,)

    filter_backends = (filters.DjangoFilterBackend,)

    @action(methods=['get', ],
            detail=False,
            permission_classes=[AllowAny, ],)
    def first_names(self, *args, **kwargs):
        """Метод описывающий реализацию скачивания рецепта в txt формате"""
        first_names = self.queryset.values_list(
            'people_on_photo__first_name', flat=True).distinct()
        return Response(first_names, status=status.HTTP_200_OK)
