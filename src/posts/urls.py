from django.conf.urls import url
from django.contrib import admin

from .views import(
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)
urlpatterns = [
    #from posts import views as post_view -> url(r'^posts/$', post_view.post_home),
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    #(?P<id>\d+)/ new printer with name of ID, only except the digit
    #?P means new pointer, which in <> means pointer name views' post_detail id should be change and models' kwargs, too
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', post_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
