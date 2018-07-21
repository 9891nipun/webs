from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Movie

class Index1View(generic.ListView):
    template_name = 'movie2/index1.html'
    def get_queryset(self):
        return Movie.objects.all()

class Index2View(generic.DetailView):
    model = Movie
    template_name = 'movie2/index2.html'
class MovieCreate(CreateView):
    model = Movie
    fields = ['actor','actor_movie','genre']

