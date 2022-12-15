from django.contrib import admin

from photo.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'location',
        'description',
        'date',
    )
    list_editable = (
        'image',
        'description',
    )
    list_display_links = (
        'location',
    )
