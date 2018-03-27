from django.db import models
from django.core.urlresolvers import reverse
import os
# Create your models here.
#def get_image_path(instance, filename):
#    return os.path.join('posts', str(instance.id), filename)

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    #profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id}) #kwargs固定用法
