from django.conf.urls import url
from mainapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.view_category, name='category'),
    url(r'^issue/(?P<issue_name_slug>[\w\-]+)/$', views.view_issue, name='issue')
]