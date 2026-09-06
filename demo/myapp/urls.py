from django.urls import path, include
from . import views
urlpatterns=[
    #to connect a url to specific path or view
    path("",views.home,name="home") ,#base url here we call home view and display it 
    path("todos/",views.todos,name="Todos")
]