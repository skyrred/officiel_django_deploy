from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import permalink
class category(models.Model):
	name = models.CharField(max_length = 255 , )
	slug = models.SlugField(unique = True, max_length=255 , )
	def __str__(self):
		return "%s" % self.name
	@permalink
	def get_absolute_url(self):
		return ("category_view_blog" , None , {'slug':self.slug})
class Post(models.Model):
	category = models.ForeignKey(category , on_delete = models.CASCADE , null=True)
	title = models.CharField(max_length = 255)
	slug = models.SlugField(unique = True , max_length=255)
	url = models.CharField(max_length = 500 , default= False)
	description = models.CharField(max_length = 200)
	content = models.TextField()
	published = models.BooleanField(default = True)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return '%s' % self.title
	#def get_absolute_url(self):
		#return reverse('blog_pst', args=[self.slug])
	@permalink
	def get_absolute_url(self):
		return ("blog_post" ,None ,{'slug':self.slug})

#	def get_url(self):
		#return reverse("blog.views.post" , args = self.slug)
#def get_absolute_url(self):
		#global slg
		#slg = self.slug
		#return reverse('blog.views.post',args = slg)
class Meta:
	ordering = ['-created']
class Post2(models.Model):
	category = models.ForeignKey(category , on_delete = models.CASCADE , null=True)
	title = models.CharField(max_length = 255)
	slug = models.SlugField(unique = True , max_length=255)
	url = models.CharField(max_length = 500)
	description = models.CharField(max_length = 200)
	content = models.TextField()
	published = models.BooleanField(default = True)		
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return '%s' % self.title
	@permalink
	def get_absolute_url(self):
		return ("blog_view_post" ,None,{'slug':self.slug})
class Meta:
	ordering = ['-created']
class Sub(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	def __str__(self):
		return '%s' % self.name
class comment1(models.Model):
	post = models.ForeignKey(Post , on_delete = models.CASCADE , null = True)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	desc = models.TextField(max_length=255)
	def __str__(self):
		return '%s' % self.name
class comment2(models.Model):
	post = models.ForeignKey(Post2 , on_delete = models.CASCADE , null = True)
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	desc = models.TextField(max_length=255)
	def __str__(self):
		return '%s' % self.name



# Create your models here.
