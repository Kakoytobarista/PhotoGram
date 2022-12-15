import django_filters

from photo.models import Photo


class PhotoFilters(django_filters.FilterSet):
    people_on_photo = django_filters.CharFilter(
        field_name="people_on_photo__first_name",
        lookup_expr='contains')

    class Meta:
        model = Photo
        fields = [
                  'date',
                  'location',
                  'people_on_photo',
                  'id',
                  'author'
                  ]
