from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import permalink

class category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique = True , max_length=255)
    
    def __str__(self):
        return "%s" % (self.name)
    @permalink
    def get_absolute_url(self):
        return ('category-shop-content' ,None, {'slug' : self.slug})
    
class shop(models.Model):
    category = models.ForeignKey(category , on_delete = models.CASCADE , null=True)
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique = True , max_length = 255)
    url = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    content = models.TextField()
    published = models.BooleanField(default =True)
    created = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return "%s" % (self.name)
    @permalink
    def get_absolute_url(self):
        return("post-content" , None , {"slug" : self.slug})
    