from django.shortcuts import render, redirect, get_object_or_404
from .models import Blogs

# Create your views here.

def home(request):
    blogs = Blogs.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def createblog(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        img = request.FILES.get('img')

        blog = Blogs(title = title, desc = desc, img = img, author = request.user)
        blog.save()
        return redirect('home')

    else:
        return render(request, 'createblog.html')
    

def readblog(request, id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, 'readblog.html', {'blog': blog})

def editblog(request, id):
    blog = get_object_or_404(Blogs, id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')

        blog.title = title
        blog.desc = desc
        blog.save()

        return redirect('readblog', id=blog.id)

    return render(request, 'editblog.html', {'blog': blog})

def deleteblog(request, id):
    blog = get_object_or_404(Blogs, id=id)
    blog.delete()
    return redirect('home')