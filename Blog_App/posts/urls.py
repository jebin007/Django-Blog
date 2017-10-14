from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', "posts.views.post_list", name='list'),
    url(r'^create/$', "posts.views.post_create"),
    url(r'^(?P<slug>[\w-]+)/$', "posts.views.post_detail", name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', "posts.views.post_update", name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', "posts.views.post_delete"),
]