from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', "posts.views.post_list"),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^(?P<id>\d+)/$', "posts.views.post_detail", name='detail'),
    url(r'^update/$', "posts.views.post_update"),
    url(r'^delete/$', "posts.views.post_delete"),
]