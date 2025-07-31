#定义learning_logs 的url 模式

from django.urls import path
from . import views

app_name='learning_logs'
urlpatterns = [
    #主页
    path('', views.index,name='index'),
    path('new_topic/',views.new_topic,name='new_topic'),
    
    path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry'),
    
    # my try here
    #path('learning_logs',views.index,name='learning_logs'),
    
    # show the page oh all the topics
    path('topics/',views.topics,name='topics'),
    # show the detailed page for some specific topic
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    # used for edit the existing entries
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]