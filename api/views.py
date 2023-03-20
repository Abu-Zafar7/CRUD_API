from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import taskTodo

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/list',
        'Create': '/create-task/',
        'Detail': '/task-detail/<str:pk>/',
        'Update': '/update-task/<str:pk>/',
        'Delete': '/delete-task/<str:pk>/',
    }
    return Response(api_urls)



@api_view(['GET'])
def getlist(request):
    task = taskTodo.objects.all()
    serializer = TaskSerializer(task,many = True)

    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request,pk):
    task = taskTodo.objects.get(id = pk)
    serializer = TaskSerializer(task,many=False)

    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)    


@api_view(['DELETE'])
def delete_task(request,pk):
    task = taskTodo.objects.get(id=pk)
    task.delete()

    return Response('Task successfully deleted')



@api_view(['POST'])
def update_task(request,pk):
    task = taskTodo.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    
    