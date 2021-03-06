"""trydjango19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from posts import views as post_view -> url(r'^posts/$', post_view.post_home),
urlpatterns = [
    url(r'^admin/', admin.site.urls), #修改路徑
    url(r'^posts/', include("posts.urls", namespace='posts')), #namespace讓不同命名空間可以有相同名字，但其他連結前方須加上"posts:"，寫在include裡
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
