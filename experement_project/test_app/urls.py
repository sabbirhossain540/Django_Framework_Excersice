from django.conf.urls import url
from test_app import views

#TEMPLATE TAGGING
app_name = 'test_app'

urlpatterns = [
    url(r'^userlist/$',views.userlist,name='userlist'),
    url(r'^other/$',views.other,name='other')
]
