from django.urls import path

from . import views

app_name = 'photo'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('photo/<int:photo_id>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('create/', views.PhotoCreateView.as_view(), name='photo_create'),
    path('photo/delete/<int:photo_id>/', views.PhotoDeleteView.as_view(), name='photo_delete'),
]
