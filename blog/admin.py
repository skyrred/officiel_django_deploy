from django.contrib import admin
from blog.models import Post,Post2,category,Sub,comment1,comment2


class PostAdmin(admin.ModelAdmin):
	# fields display on change list
	list_display = ['title', 'description']
	# fields to filter the change list with
	list_filter = ['published', 'created']
	# fields to search in change list
	search_fields = ['title', 'description', 'content']
	# enable the date drill down on change list
	date_hierarchy = 'created'
	# enable the save buttons on top on change form
	save_on_top = True
	# prepopulate the slug from the title - big timesaver!
	prepopulated_fields = {"slug": ("title",)}
	# Register your models here.
class categoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Post,PostAdmin)
admin.site.register(Post2,PostAdmin)
admin.site.register(category,categoryAdmin)
admin.site.register(Sub)
admin.site.register(comment1)
admin.site.register(comment2)
