from django.conf.urls import url
from mainapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.view_category, name='category'),
    url(r'^issue/(?P<issue_name_slug>[\w\-]+)/$', views.view_issue, name='issue'),
    url(r'^search_dictionary/$', views.search_dictionary, name="search_dictionary"),
    url(r'^search/$', views.search, name='search'),
    url(r'^dictionary/', views.dictionary, name='dictionary'),
    url(r'^local_help/', views.local_help, name='local_help'),
    url(r'^talk_to_someone/', views.talk_to_someone, name='talk_to_someone')
]