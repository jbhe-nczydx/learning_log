'''为应用程序accounts定义的url 模式'''
from django.urls import path , include
from . import views

app_name ='accounts'
urlpatterns =[
    path ('',include('django.contrib.auth.urls')),
   # path('accounts/', include('django.contrib.auth.urls')), #add by me for try 20250726
   # here is the page for registration
    path ('register/',views.register,name='register'),
] 