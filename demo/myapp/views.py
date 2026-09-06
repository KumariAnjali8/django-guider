from django.shortcuts import render , HttpResponse
def home(request):
    #return HttpResponse("hello world")
    return render(request,"home.html")
# Create your views here.
#here views is like a function which returns a response here that would be diaplayed on the website which should be connected to our app through url and routes