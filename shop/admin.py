from django.contrib import admin
from shop.models import shop,category
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
	# fields display on change list
	list_display = ['name', 'description']
	# fields to filter the change list with
	list_filter = ['published', 'created']
	# fields to search in change list
	search_fields = ['name', 'description', 'content']
	# enable the date drill down on change list
	date_hierarchy = 'created'
	# enable the save buttons on top on change form
	save_on_top = True
	# prepopulate the slug from the title - big timesaver!
	prepopulated_fields = {"slug": ("name",)}
	# Register your models here.
class categoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
    
admin.site.register(shop,ShopAdmin)
admin.site.register(category,categoryAdmin)