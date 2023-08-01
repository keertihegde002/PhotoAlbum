from django.shortcuts import render
from .models import Category,Photo
# Create your views here.
def gallery(request):
    categories=Category.objects.all()
    photos=Photo.objects.all()
    context={'categories': categories,'photos': photos} 
    return render(request, 'photos/gallery.html',context)

def viewPhoto(request,pk):
    photos=Photo.objects.get(id=pk)
    context={'photos': photos} 
    return render(request, 'photos/photo.html',context)

def addPhoto(request):
    return render(request, 'photos/add.html')
