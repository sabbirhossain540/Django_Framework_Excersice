from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'content':"Hello I am Sabbir"}
    return render(request,'test_app/index.html',context=my_dict)
    #return HttpResponse("Hello World")
