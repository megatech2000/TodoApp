from . import  views
from django.urls import path,include

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.update,name='update')
]
