from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import movie
# Create your views here.
def update(request,id) :
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'movie':Movie,'form':form})


def add_movie(request):
    if request.method== 'POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        image=request.FILES['img']
        Movie=movie(name=name,desc=desc,year=year,image=image)
        Movie.save()
        return redirect("/")
    return render(request,'add.html')
def index(request):
    obj=movie.objects.all()
    context={
        'result':obj
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    obj=movie.objects.get(id=movie_id)

    return render(request,'detail.html',{'movie':obj})
def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect("/")
    return render(request,'delete.html')