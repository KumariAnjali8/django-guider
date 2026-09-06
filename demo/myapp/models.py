from django.db import models

# Create your models here.
#create a db model that we access from django (it provides orm )
#define orm
#basically whatever we can write python code to create a model we create here would help us to craete a model in structural db schema like SQL
#this is also known as migration -automated code that create corresponding model in backend db


class TodoItem(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
#register this model in admin panel and perform migration -to have this model exist in some db schema