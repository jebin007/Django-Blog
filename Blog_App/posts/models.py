from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.conf import settings
# Create your models here.

def upload_location(instance, filename):
    return "{}/{}".format(instance.id, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field='width_field', height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(self.id)
            self.save() 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})


    class Meta:
        ordering = ['-timestamp', '-updated']