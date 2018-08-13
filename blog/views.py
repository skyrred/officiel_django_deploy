from django.shortcuts import render_to_response ,render,get_object_or_404,redirect,HttpResponse
from blog.models import *
import smtplib as p
from django.core.files import File
import random
import datetime
import requests
from django.views.decorators.csrf import csrf_exempt
#from datetime import datetime
import json


num_date = datetime.datetime.today()



def index(request):
	posts = Post.objects.all()[:3]
	return render(request ,'indexx.html',{'posts':posts})



@csrf_exempt
def get_message(request):
    try:
        print("here")
        if request.method == "POST":
            data  = json.loads(bytes.decode(request.body))
            print(data)
            if data["object"] == "page":

                for entry in data["entry"]:
                    for messaging_event in entry["messaging"]:

                        if messaging_event.get("message"):  # someone sent us a message

                            sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                            recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                            message_text = messaging_event["message"]["text"]  # the message's text

                            send_message(sender_id, "roger that!")

                        if messaging_event.get("delivery"):  # delivery confirmation
                            pass

                        if messaging_event.get("optin"):  # optin confirmation
                            pass

                        if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                            pass
            return HttpResponse(json.dumps({
                "status":"200",
                "status_message":"well done",
                }))
        elif request.method == "GET":
            if request.GET.get("hub.mode") == "subscribe" and request.GET.get("hub.challenge"):
                if not request.GET.get("hub.verify_token") == "test":
                    return HttpResponse("Verification token mismatch")
                return HttpResponse(request.GET.get("hub.challenge"))

            return HttpResponse("Hello world")





    except Exception as e:
        print(str(e))

def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": "EAADp8CuGpZBEBALjDeDFwxbxUFXTRSMsZBrZCpLZBBo3IlOgwiDE9LtZBYZAtNYYZCTcGT42Q25I3CgwGD3FRCq7e9kyg5XufkviVSJhDlZAGWx6b8qhj18ZCPE8SYEXEu3LytI0Hg4443y2sLc0dReh05fZAUooAUuSdfTni174tVZCqzL8BCP3ySo"
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def blog(request):
	posts = Post.objects.filter(published = True)
	posts2 = Post2.objects.filter(published = True)
	categorys = category.objects.all()
	number = str(Sub.objects.count())
	return render(request , 'blog.html' , {'posts':posts,'posts2':posts2,'category':categorys,'num':number})
def view_blog_post(request , slug):
	count = []
	post = get_object_or_404(Post , slug = slug)
	if (request.method == 'POST'):
		name = request.POST.get('name' , None)
		if (len(name)!= 0):
			email = request.POST.get('email' , None)
			cmnt = request.POST.get('comment',None)
			c = post.comment1_set.create(name = name , email = email , desc = cmnt)
			c.save()
	comment = comment1.objects.filter(post = post)
	posts = Post.objects.all()
	#if len(posts) > 3:
		#while len(count) <= 3:
			#post_random = random.choice(posts)
			#count.append(post_random)
		#return render(request,'testpost.html',{'post':post,'comment':comment , 'posts':count})
	#else:
	return render(request,'testpost.html',{'post':post,'comment':comment , 'posts':posts})



def skyfoot_index_blog(request):
    posts = skyfoot_post.objects.filter(published = True).order_by('-created')
    thread_posts = skyfoot_post.objects.filter(published = True).order_by('-views')
    results_data =  match_results.objects.all().order_by('-date')
    day = num_date.day
    results = []
    ############## posts variables ##############
    post_pages = {}
    post_list = []
    #############################################
    for res in results_data:
    	date_val = res.date.day
    	if int(date_val) == int(day):
    		results.append(res)
    	else:
    		pass
    print(results)

    
    groups = []
    groups.append(group.objects.filter(rank=1))
    groups_dict = []
    for each_group in groups:
    	team_list = []
    	team_list.append(each_group)
    	teams = team.objects.filter(group = each_group).order_by('-Points')
    	for each_team in teams:
    		team_list.append(each_team)
    	
    	groups_dict.append(team_list)

    #if len(posts) > 10:
        #posts = skyfoot_post.objects.filter(published = True).order_by('-created')[0:9]


    ######### code for setting every page to their posts #############
    counter_post = 1
    counter = 1
    for post in posts:
        post_list.append(post)
        if counter % 10 == 0:
            post_pages[counter_post] = post_list
            post_list = []
            counter_post += 1
        counter += 1

    if len(post_list) > 0 :
        post_pages[counter_post] = post_list
        post_list = []

    ############### checking for page #####################
    if (request.method == "GET"):
        page = request.GET.get('page',None)
        if page != None:
            posts = post_pages[int(page)]
        else:
            posts = post_pages[1]

    else:
        posts = post_pages[1]

    pages = [x for x in post_pages.keys()]

    ###################################################################

    if len(thread_posts) > 6:
        thread_posts = skyfoot_post.objects.filter(published = True).order_by('-views')[0:5]
    categorys = skyfoot_cat.objects.all()
    shirt_posts = shirts.objects.all().order_by('-created')
    shirt_list = []
    each_shirt = []
    for shirt in shirt_posts:
    	each_shirt.append(shirt)
    	if int(shirt.num_id) % 3 == 0:
    		shirt_list.append(each_shirt)
    		each_shirt = []
    if len(each_shirt) != 0:
    	shirt_list.append(each_shirt)
    	each_shirt = []

    print(shirt_list)
    #print(len(shirt_list))
    num = [x for x in range(int(len(shirt_list)))]
    print(num)
    post_num = [x for x in range(len(thread_posts))]
    results_num = [x for x in range(int(match_results.objects.count()))]
    groups_num = [x for x in range(int(group.objects.count()))]
    #print(groups_dict)
    return render(request,"test_temp.html",{"posts":posts,
    	"categories":categorys,
    	'shirts':shirt_list,
    	'num':num,
    	"thread_posts":thread_posts,
    	"post_num":post_num,
    	"results":results,
    	"results_num":results_num,
    	"groups_dict" : groups_dict,
    	"groups_num":groups_num,
    	"shirt_posts":shirt_posts,
        "pages" :pages,
    	

    	})

    #return render(request,"test_temp.html",{"posts":posts,"categories":categorys,'shirts':shirt_posts,'num':num})
def skyfoot_view_category(request,slug):
    categories = get_object_or_404(skyfoot_cat ,slug = slug)
    posts = skyfoot_post.objects.filter(published=True,category=categories).order_by('-created')
    thread_posts = skyfoot_post.objects.filter(published = True).order_by('-views')
    results_data =  match_results.objects.all().order_by('-date')
    day = num_date.day
    results = []
    ############## posts variables ##############
    post_pages = {}
    post_list = []
    #############################################
     ######### code for setting every page to their posts #############
    counter_post = 1
    counter = 1
    for post in posts:
        post_list.append(post)
        if counter % 10 == 0:
            post_pages[counter_post] = post_list
            post_list = []
            counter_post += 1
        counter += 1

    if len(post_list) > 0 :
        post_pages[counter_post] = post_list
        post_list = []

    ############### checking for page #####################
    if (request.method == "GET"):
        page = request.GET.get('page',None)
        if page != None:
            posts = post_pages[int(page)]
        else:
            posts = post_pages[1]

    else:
        posts = post_pages[1]

    pages = [x for x in post_pages.keys()]

    ###################################################################
    for res in results_data:
    	date_val = res.date.day
    	if int(date_val) == int(day):
    		results.append(res)
    	else:
    		pass
    print(results)

    
    groups = []
    groups.append(group.objects.filter(rank=1))
    groups_dict = []
    for each_group in groups:
    	team_list = []
    	team_list.append(each_group)
    	teams = team.objects.filter(group = each_group).order_by('-Points')
    	for each_team in teams:
    		team_list.append(each_team)
    	
    	groups_dict.append(team_list)

    if len(posts) > 10:
        posts = skyfoot_post.objects.filter(published=True,category=categories).order_by('-created')[10]
    if len(thread_posts) > 6:
        thread_posts = skyfoot_post.objects.filter(published = True).order_by('-views')[6]
    categorys = skyfoot_cat.objects.all()
    shirt_posts = shirts.objects.all().order_by('-created')
    shirt_list = []
    each_shirt = []
    for shirt in shirt_posts:
    	each_shirt.append(shirt)
    	if int(shirt.num_id) % 3 == 0:
    		shirt_list.append(each_shirt)
    		each_shirt = []
    if len(each_shirt) != 0:
    	shirt_list.append(each_shirt)
    	each_shirt = []

    print(shirt_list)
    #print(len(shirt_list))
    num = [x for x in range(int(len(shirt_list)))]
    print(num)
    post_num = [x for x in range(len(thread_posts))]
    results_num = [x for x in range(int(match_results.objects.count()))]
    groups_num = [x for x in range(int(group.objects.count()))]
    #print(groups_dict)
    return render(request,"test_temp.html",{"posts":posts,
    	"categories":categorys,
    	'shirts':shirt_list,
    	'num':num,
    	"thread_posts":thread_posts,
    	"post_num":post_num,
    	"results":results,
    	"results_num":results_num,
    	"groups_dict" : groups_dict,
    	"groups_num":groups_num,
    	"shirt_posts":shirt_posts,
        "pages":pages,
    	

    	})
    

def get_data(post):
    categorys = skyfoot_cat.objects.all()
    comment = skyfoot_comment.objects.filter(post=post)
    new_post = skyfoot_post.objects.filter(published=True).order_by('-created')[0:3]
    thread_post = skyfoot_post.objects.filter(published=True).order_by('-views')[0:3]
    data = {
        'post':post,
        'comment':comment,
        'new_posts':new_post,
        'thread_posts':thread_post,
        'categories':categorys
    }
    return data
def check_comment(request,post):
    if (request.method == 'GET'):
        name = request.GET.get('name',None)
        if name != None:
            if (len(name)!=0):
                email = request.GET.get('name',None)
                cmnt = request.GET.get('comment',None)
                c = post.skyfoot_comment_set.create(name=name,email=email,desc=cmnt)
                c.save()
    
#post = get_object_or_404(skyfoot_post, slug = slug)
def view_post_2(request , slug):
    post = get_object_or_404(skyfoot_post,slug=slug)
    post.views += 1
    post.save()
    check_comment(request,post)
    data_dic = get_data(post)
    
    return render_to_response('test_temp_con.html',data_dic)
    
    #categorys = skyfoot_cat.objects.all()
	#comment = post.comment2_set.all()
    #categorys = skyfoot_cat.objects.all()
	#comment = skyfoot_comment.objects.filter(post = post)
    #new_posts = skyfoot_post.objects.filter(published=True).order_by('-created')[0:3]
    #thread_posts = skyfoot_post.objects.filter(published=True).order_by('-views')
    #data = {'post':post,
            #'comment':comment,
            #'new_posts':new_posts,
            #'thread_posts':thread_posts,
           #'categories':categorys}
    #data = get_data()
	#return render_to_response('test_temp_con.html',data)
def post(request,slug):
	post = get_object_or_404(Post ,slug=slug)
	#comment = post.comment1_set.all()
	
	return render(request,'post.html',{'post':post,'comment':comment})
def about(request):
	return render(request,'about.html')
def sending(request):
	if (request.method == 'GET'):
		name = request.GET.get('name',None)
		about = request.GET.get('email',None)
		description = request.GET.get('description',None)
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
		server.login("teamsky.work@gmail.com","nefdaaxgeddqxxyv")
		server.sendmail("teamsky.work@gmail.com","skyfoot18@gmail.com",msg)
        #server.lgoin("teamsky.work@gmail.com","teamskywork123")
        #server.sendmail("skytechno.work@gmail.com","sky.red2212@gmail.com",msg)
		#server.login("skytechno.work@gmail.com","skytech123")
		#server.sendmail("skytechno.work@gmail.com","sky.red2212@gmail.com",msg)
        
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
	if (request.method == 'GET'):
		name = request.GET.get('name',None)
		email = request.GET.get('email',None)
		q = Sub(name = name , email=email)
		q.save()
		file = open("maillist.txt","a")
		file.write("\n")
		file.write(name)
		file.write("\n")
		file.write(email)
		file.close()
		return  redirect('https://skyteam.herokuapp.com/blog')
	else:
		return redirect('https://www.google.com')
def share(request):
	maillist = Sub.objects.all()
	about = "New post"
	url = "https://skyteam.herokuapp.com/news"
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
		return redirect("https://skyteam.herokuapp.com")
def news(request):
	posts = Post.objects.filter(published = True)[0:6]
	posts2 = Post2.objects.filter(published = True)[0:6]
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
def skyapp_index(request):
	return render(request,'skyapp.html')

def skyapp_pay(request):
	if request.method == "POST":
		name = request.POST.get("name")
		surname = request.POST.get("surname")
		email = request.POST.get("email")
		password = request.POST.get("password")
		new_user = app_user(name=name,surname=surname,email = email , password=password)
		new_user.save()
	return redirect('http://www.mediafire.com/file/sv05pehu93s986n/skydrop%282%29.zip')


def skyfoot_index(request):
    new = skyfoot_news.objects.all().order_by('created')[0:3]
    #categories = get_object_or_404(category ,slug = "world-cup")
    posts = skyfoot_post.objects.filter(published=True).order_by('created')[0:3]
    return render(request,"skyfoot_index.html",{"news":new,"posts":posts})
    #return render(request,"skyfoot_index.html",{"news":new,"posts":posts})


def showtables(request):
	all_groups = group.objects.all().order_by("rank")
	dates = match_dates.objects.all().order_by("date")


	return render(request,"tables.html",{
		"all_groups":all_groups,
		"dates" : dates,
		})


def tvlive(request):
	server = servers.objects.filter(published =True)

	return render(request,"Ip_tv.html",{
		"servers":server,
		})