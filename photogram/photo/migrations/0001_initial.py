# Generated by Django 4.1.4 on 2022-12-15 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='field for add photo', upload_to='photo/', verbose_name='photo')),
                ('location', models.CharField(help_text='field for geo location', max_length=120, verbose_name='geo location')),
                ('description', models.TextField(help_text='field for description abot photo', max_length=255, verbose_name='description about photo')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date of created')),
                ('author', models.ForeignKey(help_text='field for author of photo', on_delete=django.db.models.deletion.CASCADE, related_name='photo_author', to=settings.AUTH_USER_MODEL, verbose_name='author of photo')),
                ('people_on_photo', models.ManyToManyField(blank=True, help_text='field for identifying people in the photo', related_name='photo', to=settings.AUTH_USER_MODEL, verbose_name='people on photo')),
            ],
        ),
        migrations.AddIndex(
            model_name='photo',
            index=models.Index(fields=['date', 'author', 'location'], name='photo_photo_date_3d6905_idx'),
        ),
    ]
