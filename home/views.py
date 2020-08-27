from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
   # messages.success(request,"your message has been sucessfully sent")
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']
        print(name,email,phone,content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<5:
            messages.error(request,"Please fill the form correctly")
        else:
            contact=Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"your message has been sucessfully sent")

    return render(request,'home/contact.html')

def search(request):
    query= request.GET['query']
    if len(query)>50:
        allPosts=Post.objects.none()
    else:
        allPostsTitle =Post.objects.filter(title__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPostsAuthor =Post.objects.filter(author__icontains=query)
        allPosts =allPostsTitle.union(allPostsContent).union(allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request,"No search results found.Please refine your query")
    params={'allPosts':allPosts,'query':query}
    return render(request,'home/search.html',params)

def Signup(request):
    if  request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username)< 2 or len(fname)<5 or len(lname)<3 or len(email)<3  or pass1 !=pass2:
            messages.error(request," invalid form")
            return redirect('/')
        else:
            myuser = User.objects.create_user(username,email,pass1)
            print(myuser)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            messages.success(request,'Your iCoder account has been created sucessfuly')
            return redirect('home')
    else:
        return HttpResponse('404- Not Found')

def user_login(request):
    if request.method=='POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request,"Successfully Logged in")
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials, Please try again')
            return redirect('home')

    return HttpResponse('404- Not Found')

def user_logout(request):
    logout(request)
    messages.success(request,"Successfully Logged out")
    return redirect('home')