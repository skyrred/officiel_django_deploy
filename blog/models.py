from django.db import models
from django.core.urlresolvers import reverse
from django.db.models import permalink




class group(models.Model):
	name = models.CharField(max_length = 250)
	rank = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

class team(models.Model):
	group = models.ForeignKey(group , on_delete = models.CASCADE)
	country = models.CharField(max_length = 150)
	win = models.IntegerField()
	Lose = models.IntegerField()
	Tie = models.IntegerField()
	Points = models.IntegerField()

	def __str__(self):
		return self.country



class match_results(models.Model):
	date = models.DateTimeField()
	match1 = models.CharField(max_length = 120 , null = True)
	country1 = models.CharField(max_length = 120 , null = True)
	result_1 = models.CharField(max_length = 120 , null = True)
	country2 = models.CharField(max_length = 120 , null = True)
	match2 = models.CharField(max_length = 120 , null = True)
	country3 = models.CharField(max_length = 120 , null = True)
	result_2 = models.CharField(max_length = 120 , null = True)
	country4 = models.CharField(max_length = 120 , null = True)
	match3 = models.CharField(max_length = 120 , null = True)
	country5 = models.CharField(max_length = 120 , null = True ) 
	result_3 = models.CharField(max_length = 120 , null = True)
	country6 = models.CharField(max_length = 120 , null = True)
	match4 = models.CharField(max_length = 120 , null = True)
	country7 = models.CharField(max_length = 120 , null = True)
	result_4 = models.CharField(max_length = 120 , null = True)
	country8 = models.CharField(max_length = 120 , null = True)
	match5 = models.CharField(max_length = 120 , null = True)
	country9 = models.CharField(max_length = 120 , null = True)
	result_5 = models.CharField(max_length = 120 , null = True)
	country10 = models.CharField(max_length = 120 , null = True)


	def __str__(self):
		return str(self.date)
    

class flags(models.Model):
	country_name = models.CharField(max_length = 120)
	flag_url = models.CharField(max_length = 250)

	def __str__(self):
		return self.country_name
		
    

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
	@permalink
	def go_home_blog(self):
		return ("blog_index",None)

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
    #views = models.AutoField(default = 0)
	content = models.TextField()
	published = models.BooleanField(default = True)		
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return '%s' % self.title
	@permalink
	def get_absolute_url(self):
        #self.views += 1
		return ("skyfoot_view_post" ,None,{'slug':self.slug})
    

class skyfoot_cat(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(unique=True,max_length=255)
    def __str__(self):
        return "%s" % self.name
    @permalink
    def get_absolute_url(self):
        return ("category_view_skyfoot" , None , {'slug':self.slug})
class skyfoot_post(models.Model):
    category = models.ForeignKey(skyfoot_cat , on_delete = models.CASCADE , null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True , max_length = 255)
    url = models.CharField(max_length = 500)
    description = models.CharField(max_length = 200)
    views = models.IntegerField(default = 0)
    content = models.TextField()
    published = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    @permalink
    def get_absolute_url(self):
        return ("skyfoot_view_post" , None,{'slug':self.slug})
class Meta:
	ordering = ['-created']

class skyfoot_comment(models.Model):
    post = models.ForeignKey(skyfoot_post , on_delete = models.CASCADE , null = True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    def __str__(self):
        return '%s' % self.name
    
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

class app_user(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	paid = models.BooleanField(default=False)


class skyfoot_news(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class shirts(models.Model):
    url = models.CharField(max_length=255)
    url_post = models.CharField(max_length=255)
    title = models.CharField(max_length=255 , default = " ")
    description = models.CharField(max_length = 255 , default = " ")
    price = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add = True)
    num_id = models.IntegerField(default = 0)
    

class match_dates(models.Model):
	date = models.DateField()
	idd = models.IntegerField()


	def __str__(self):
		return str(self.idd)



class all_matches(models.Model):
	match_date = models.ForeignKey(match_dates , on_delete = models.CASCADE , default = None)
	country_1 = models.CharField(max_length=100 , default = None)
	result = models.CharField(max_length=100 , default = None)
	country_2 = models.CharField(max_length=100 , default = None)

	def __str__(self):
		title = self.country_1 + "||" + self.country_2
		return title

# Create your models here.
