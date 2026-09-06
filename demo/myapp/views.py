from django.shortcuts import render , HttpResponse
from .models import TodoItem
def home(request):
    #return HttpResponse("hello world")
    return render(request,"home.html")
# Create your views here.
#here views is like a function which returns a response here that would be diaplayed on the website which should be connected to our app through url and routes

def todos(request):
    items=TodoItem.objects.all()
    return render(request,"todos.html",{"todos":items })