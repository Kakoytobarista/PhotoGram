from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('description', 'image', 'location',
                  'people_on_photo')


# class CommentForm(forms.ModelForm):
#
#     class Meta:
#         model = Comment
#         fields = ('text',)
