
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from .models import Film
from .forms import FilmForm
from django.shortcuts import redirect, get_object_or_404, render

class FilmListView(ListView):
    model = Film
    template_name = 'films/film_list.html'
    context_object_name = 'films'
    paginate_by = 3

class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/film_detail.html'
    context_object_name = 'film'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save(update_fields=['views_count'])  
        return obj

class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/film_create.html'
    success_url = reverse_lazy('films:film_list')

class FilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/film_update.html'
    success_url = reverse_lazy('films:film_list')

class FilmDeleteView(DeleteView):
    def get(self, request, id):
        film = get_object_or_404(Film, id=id)
        film.delete()
        return redirect('films:film_list')
    
class FilmSearchView(ListView):
    model = Film
    template_name = 'films/film_search.html'  
    context_object_name = 'films'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Film.objects.filter(Q(title__icontains=query))
        return Film.objects.none()  