#from django.shortcuts import render
from django.shortcuts import render_to_response ,render,get_object_or_404,redirect
from shop.models import shop,category
# Create your views here.

def shope(request):
    articles = shop.objects.filter(published = True)
    categories = category.objects.all()
    return render(request , "shop.html" , {"articles" : articles,"category":categories})
def view_category_shop(request,slug):
	category = get_object_or_404(category , slug = slug)
	articles = shop.objects.filter(category = category)
	categories = shop.objects.all()
	return render(request , 'shop.html' , {"articles" : articles,"category":categories})

	#category = get_object_or_404(category , slug = slug)
    #articles = shop.objects.filter(category = category)
    #cateogries = category.objects.all()
    #return render(request , "shop.html" , {"articles" : articles,"category":categories})
def view_item(request,slug):
    item = get_object_or_404(shop ,slug = slug)
    return render(request , "shop_item.html", {"item":item})
def search(request):
 	if (request.method == 'get'):
 		keyword = request.GET.get('search')
 		articles = shop.objects.filter(name__icontains = keyword)
 		cateogries = category.objects.all()
 		return render(request , 'shop.html', {"articles": articles , " category":categories})
 	