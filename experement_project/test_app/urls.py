from django.conf.urls import url
from test_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
