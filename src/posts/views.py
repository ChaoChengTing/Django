#view handle the request and return response
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import PostForm
from .models import Post #資料庫加入views

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully Created")
    context = { #加在此作為html呼叫使用 沒加的話html不會顯示任何資訊
        "title": "Create",
        "form": form
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None): #當網址後要新增東西 這裡也要新增 retrieve 此id與下方id意義不同
    #instance = Post.objects.get(id=11) #會顯示整個錯誤訊息
    instance = get_object_or_404(Post, id=id) #僅顯示404錯誤 #Post代表整個資料庫 所以後面可以放屬姓名="blablabla"
    context = {
        "title": instance.title,
        "content": instance.content,
        "updated": instance.updated,
        "timestamp": instance.timestamp,
        "id": instance.id,
        "instance": instance
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all().order_by('-timestamp')
    #if request.user.is_authenticated():
    #    context = {
    #        "title": "My User List"
    #    }
    #else:
    context = {
        "object_list": queryset,
        "title": "Article List"
    }
    return render(request, "index.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id) #僅顯示404錯誤 #Post代表整個資料庫 所以後面可以放屬姓名="blablabla"
    form = PostForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #messages.success(request, "Successfully saved")
        messages.success(request, "Successfully saved <a href='#'>Item</a>", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:list")
