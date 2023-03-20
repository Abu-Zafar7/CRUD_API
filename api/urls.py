from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiOverview,name= 'api_view'),
    path('list/',views.getlist, name= 'getlist'),
    path('task-detail/<str:pk>/',views.task_detail,name='task-detail'),
    path('create-task/',views.create_task,name='create-task'),
    path('delete-task/<str:pk>/',views.delete_task,name='delete-task'),
    path('update-task/<str:pk>/',views.update_task,name='update-task')
]