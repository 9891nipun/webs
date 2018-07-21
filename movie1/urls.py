from django.conf.urls import url
from . import views
app_name='movie1'

urlpatterns = [
    #/movie1/
    url(r'^$', views.Index1View.as_view(), name='index1'),
    #/movie1/<a.id>

    url(r'^(?P<pk>[0-9]+)/$', views.Index2View.as_view(), name='detail'),
    url(r'movie1/add/$', views.MovieCreate.as_view(), name='movie-add')



]