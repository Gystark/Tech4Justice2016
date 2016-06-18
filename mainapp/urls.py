from django.conf.urls import url
from mainapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.view_category, name='category'),
    url(r'^get_issues/', views.get_issues, name='get_issues'),
    url(r'^search/', views.search, name='search'),
    url(r'^dictionary/', views.dictionary, name='dictionary'),
    url(r'^local_help/', views.local_help, name='local_help'),
    url(r'^talk_to_someone/', views.talk_to_someone, name='talk_to_someone')
]