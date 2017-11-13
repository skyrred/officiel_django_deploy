from django.shortcuts import render_to_response ,render,get_object_or_404,redirect
from blog.models import Post,Post2,category,Sub,comment1,comment2
import webbrowser
import smtplib as p
from django.core.files import File


def index(request):
	posts = Post.objects.all()
	return render(request ,'indexx.html',{'posts':posts})
def blog(request):
	posts = Post.objects.filter(published = True)
	posts2 = Post2.objects.filter(published = True)
	categorys = category.objects.all()
	number = str(Sub.objects.count())
	return render(request , 'blog.html' , {'posts':posts,'posts2':posts2,'category':categorys,'num':number})
def view_blog_post(request , slug):
	post = get_object_or_404(Post , slug = slug)
	if (request.method == 'POST'):
		name = request.POST.get('name' , None)
		if (len(name)!= 0):
			email = request.POST.get('email' , None)
			cmnt = request.POST.get('comment',None)
			c = post.comment1_set.create(name = name , email = email , desc = cmnt)
			c.save()
	comment = comment1.objects.filter(post = post)
	return render(request,'testpost.html',{'post':post,'comment':comment})

def view_post_2(request , slug):
	post = get_object_or_404(Post2 , slug = slug)
	if (request.method == 'POST'):
		name = request.POST.get('name' , None)
		if (len(name)!= 0):
			email = request.POST.get('email' , None)
			cmnt = request.POST.get('comment',None)
			c = post.comment1_set.create(name = name , email = email , desc = cmnt)
			c.save()
	#comment = post.comment2_set.all()
	comment = comment2.objects.filter(post = post)
	return render_to_response('post.html',{'post':post,'comment':comment})
def post(request,slug):
	post = get_object_or_404(Post ,slug=slug)
	#comment = post.comment1_set.all()
	
	return render(request,'post.html',{'post':post,'comment':comment})
def about(request):
	return render(request,'about.html')
def sending(request):
	if (request.method == 'POST'):
		name = request.POST.get('name',None)
		about = request.POST.get('email',None)
		description = request.POST.get('description',None)
		msg ="""From: From skyteam.work@gmail.com
To: %r
MIME-Version: 1.0
Content-type: text/html
Subject: BUG repport about (%a)
<h1> Message :</h1>
<p>%s</p>

"""	% (name,about,description)	
		server = p.SMTP("smtp.gmail.com",587)
		server.starttls()
		server.login("teamsky.work@gmail.com","teamskywork123")
		server.sendmail("teamsky.work@gmail.com","sky.red2212@gmail.com",msg)
		posts = Post.objects.all()
		return render(request ,'indexx.html',{'posts':posts})
def send(request):
	return render(request , 'sending.html')
def view_category(request,slug):
	categories = get_object_or_404(category ,slug = slug)
	categorys = category.objects.all()
	posts = Post.objects.filter(category = categories)
	posts2 = Post2.objects.filter(category = categories)
	number = str(Sub.objects.count())
	return render(request , 'blog.html',{'category':categorys,'posts':posts,'posts2':posts2,'num':number})
def subscribe(request):
	if (request.method == 'POST'):
		name = request.POST.get('name',None)
		email = request.POST.get('email',None)
		q = Sub(name = name , email=email)
		q.save()
		file = open("maillist.txt","a")
		file.write("\n")
		file.write(name)
		file.write("\n")
		file.write(email)
		file.close()
		return  redirect('http://127.0.0.1:8000/blog')
	else:
		return redirect('https://www.google.com')
def share(request):
	maillist = Sub.objects.all()
	about = "New post"
	url = "http://127.0.0.1:8000/news"
	server = p.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login("teamsky.work@gmail.com","teamskywork123")
	for mail in maillist:
		msg ="""From: From skyteam.work@gmail.com
To: %r
MIME-Version: 1.0
Content-type: text/html
Subject:  (%a)
<h1> Message :</h1>
<p>check our new post in \n %s</p>

"""	% (mail.name,about,url)
		server.sendmail("teamsky.work@gmail.com",mail.email,msg)
		return redirect("http://127.0.0.1:8000")
def news(request):
	posts = Post.objects.filter(published = True)[0:3]
	posts2 = Post2.objects.filter(published = True)[0:3]
	categorys = category.objects.all()
	number = str(Sub.objects.count())
	return render(request , 'blog.html' , {'posts':posts,'posts2':posts2,'category':categorys,'num':number})
# Create your views here.
def blog_search(request):
 	if (request.method == 'GET'):
 		keyword = request.GET.get('search')
 		posts = Post.objects.filter(title__icontains = keyword)
 		posts2 = Post2.objects.filter(title__icontains=keyword)
 		categorys = category.objects.all()
 		number = str (Sub.objects.count())
 		#import webbrowser
 		#webbrowser.open("www.google.com")
 		return render(request , 'blog.html' , {'posts':posts,'posts2':posts2,'category':categorys,'num':number})
