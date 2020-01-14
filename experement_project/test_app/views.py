from django.shortcuts import render
#from django.http import HttpResponse
from test_app.models import User
from test_app.forms import NewUserFrom


# Create your views here.
def index(request):
    myDict = {'Description':'This is an Online Registration System'}
    return render(request,'test_app/index.html',context=myDict)
    #return HttpResponse("Hello World")

def users(request):
    form = NewUserFrom()
    if request.method == "POST":
        form = NewUserFrom(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error From Invalid')
    return render(request,'test_app/user_form.html',{'form':form})

def userlist(request):
    user_list = User.objects.order_by('first_name')
    date_dict = {'u_list':user_list}
    return render(request,'test_app/relative.html',context = date_dict)

def other(request):
    return render(request,'test_app/other.html')
