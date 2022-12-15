from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from photo.models import Photo


class GetPhotoSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    people_on_photo = serializers.SlugRelatedField(slug_field='first_name',
                                                   read_only=True,
                                                   many=True)

    class Meta:
        model = Photo
        fields = (
                  'id',
                  'image',
                  'people_on_photo',
        )

        read_only_fields = ('__all__',)
