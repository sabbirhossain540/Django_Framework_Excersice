from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import User

# Create your views here.
def index(request):
    return render(request,'test_app/index.html')
    #return HttpResponse("Hello World")

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'test_app/userList.html',context=user_dict)
