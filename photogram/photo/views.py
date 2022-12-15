from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator


from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Photo
from .forms import PhotoForm
from core.filters import PhotoFilters


class IndexView(ListView):
    model = Photo
    template_name = 'photo/index.html'

    @method_decorator(transaction.atomic)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        filters = PhotoFilters(self.request.GET, queryset)
        return filters.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['photos'] = queryset
        return context


class PhotoDetailView(DetailView):
    template_name = 'photo/photo_detail.html'

    @method_decorator(transaction.atomic)
    def dispatch(self, *args, **kwargs):
        return super(PhotoDetailView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo = get_object_or_404(Photo,
                                  id=self.kwargs.get('photo_id'))
        peoples = photo.people_on_photo.select_related('photo').values_list(
            'first_name', flat=True)

        context['photo'] = photo
        context['peoples'] = ", ".join(i for i in peoples)
        return context

    def get_object(self, *args, **kwargs):
        post = get_object_or_404(Photo, id=self.kwargs.get('photo_id'))
        return post


class PhotoCreateView(CreateView, LoginRequiredMixin):
    model = Photo
    template_name = 'photo/create_photo.html'
    form_class = PhotoForm

    @method_decorator(transaction.atomic)
    def dispatch(self, *args, **kwargs):
        return super(PhotoCreateView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('photo:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class PhotoDeleteView(DeleteView, LoginRequiredMixin):
    model = Photo
    pk_url_kwarg = 'photo_id'
    http_method_names = ['delete', 'get', ]

    @method_decorator(transaction.atomic)
    def dispatch(self, *args, **kwargs):
        return super(PhotoDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        success_url = str(reverse_lazy('photo:index'))
        return success_url

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched
        object and then redirect to the
        success URL.
        """
        self.get_object().delete()
        return HttpResponseRedirect(reverse('photo:index'))
