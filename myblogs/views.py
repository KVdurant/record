from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
# Create your views here.
#def index(request):
#	return HttpResponse("hello,world,you're at the blog index.")
def index(request):
        posts = Post.objects.all()
 #       post_lists =[]
        now=datetime.now()
        template =get_template('myblogs/index.html')
        html=template.render(locals())
#       for count,post in enumerate(posts,1):
 #           post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
        return HttpResponse(html)
def show_post(request,slug):
    template =get_template('myblogs/post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
         return redirect('/')    