"""netmag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/y<
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url,include
from django.contrib import admin
from blog.views import *
from shop.views import *
#from blog.views import *



urlpatterns = [
    url(r'^skyadmin/', admin.site.urls),
    url(r'^blog/', blog , name="blog_index"),
    url(r'^$',index),
    url(r'^send/result/$',sending),
    url(r'^send/$',send),
    url(r'^about/$',about),
   	url(r'^view/(?P<slug>[^\.]+)/$',view_blog_post,name='blog_post'),
    url(r'^view/post/(?P<slug>[^\.]+)./$', view_post_2, name='blog_view_post'),
    url(r'^categories/(?P<slug>[^\.]+)./$',view_category, name='category_view_blog'),
    url(r'^subscribe/$',subscribe),
    url(r'^news/$',news),
    url(r'^share/$',share),
    url(r'^shop/',shope),
    url(r'^view/shop/(?P<slug>[^\.]+)/$',view_item, name='post-content'),
    url(r'^shop/category/(?P<slug>[^\.]+)/$',view_category_shop, name = 'category-shop-content'),
    url(r'^shop/search/$',search , name='search-content'),
    url(r'^search/$',blog_search ),
    url(r'^skyapp/$',skyapp_index , name='skyapp_index'),
    url(r'^skyapp/pay/$',skyapp_pay , name='skyapp_pay'),
    url(r'^skyfoot/$',skyfoot_index,name='skyfoot'),
    url(r'^skyfoot/blog/$',skyfoot_index_blog,name='skyfoot_blog'),
    url(r'^skyfoot/categories/(?P<slug>[^\.]+)./$',skyfoot_view_category, name='category_view_skyfoot'),
    url(r'^skyfoot/blog/view/(?P<slug>[^\.]+)/$',view_post_2,name='skyfoot_view_post'),
    url(r'^skyfoot/blog/tables/$',showtables,name="tables"),
    url(r'^skyfoot/blog/live/$',tvlive,name="tv"),
    url(r'^api/$',get_message,name="api_call"),
    url(r'^test/$',new_index,name="test_index"),
    url(r'^^token/$',token_handler,name="token_handler")
    #url(r'^(?P<slug>[\w\-]+)/$',view_post, name = "blog_post"),
    #url(r'^blog/view/show/(?P<slug>[^\.]+).html',post,name='blog_pst'),

	]
