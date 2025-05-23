
from django.shortcuts import render, get_object_or_404, redirect
from .models import Film, Reviews
from .forms import ReviewsForm, FilmForm

def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})

def film_detail(request, id):
    film = get_object_or_404(Film, id=id)
    reviews = Reviews.objects.filter(films_choice=film).order_by('-id')

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.films_choice = film
            review.save()
            form = ReviewsForm()
    else:
        form = ReviewsForm()

    context = {
        'film': film,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'films/film_detail.html', context)

def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('films:film_list')
    else:
        form = FilmForm()
    return render(request, 'films/film_create.html', {'form': form})

def film_update(request, id):
    film = get_object_or_404(Film, id=id)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('films:film_detail', id=film.id)
    else:
        form = FilmForm(instance=film)
    return render(request, 'films/film_update.html', {'form': form})


def film_delete(request, id):
    film = get_object_or_404(Film, id=id)
    film.delete()
    return redirect('films:film_list')