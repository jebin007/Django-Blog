from django.conf.urls import url

urlpatterns = [
    url(r'^$', "posts.views.post_home"),
]