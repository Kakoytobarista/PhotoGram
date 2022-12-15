from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Photo(models.Model):
    image = models.ImageField(verbose_name='photo',
                              upload_to='photo/',
                              blank=False,
                              help_text='field for add photo')
    location = models.CharField(verbose_name='geo location',
                                max_length=120,
                                help_text='field for geo location')
    description = models.TextField(verbose_name='description about photo',
                                   max_length=255,
                                   help_text='field for description abot photo')
    people_on_photo = models.ManyToManyField(to=User,
                                             related_name='photo',
                                             verbose_name='people on photo',
                                             blank=True,
                                             help_text='field for identifying '
                                                       'people in the photo')
    author = models.ForeignKey(to=User,
                               related_name='photo_author',
                                            verbose_name='author of photo',
                               on_delete=models.CASCADE,
                               help_text='field for author of photo')
    date = models.DateField('date of created',
                            auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['date', 'author', 'location']),
        ]
