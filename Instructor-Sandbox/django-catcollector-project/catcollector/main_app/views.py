from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Cat


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})



def cats_index(request):
    cats_list = Cat.objects.all()
    return render(request, 'cats/index.html', {
        'cats': cats_list
    })


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1> About the CatCollector </h1>')

# function home(req,res)
def home(request):
    return render(request, 'home.html')


# def home(request):
#     return HttpResponse('<h1>My First Django Route!</h1>')