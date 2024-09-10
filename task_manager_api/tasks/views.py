from django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task
from .serializers import TaskSerializer
from .google_calendar import create_google_calendar_event, delete_google_calendar_event



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        task_id = self.request.query_params.get('id', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        title = self.request.query_params.get('title', None)

        
        if task_id:
            queryset = queryset.filter(id=task_id)

       
        if start_date and end_date:
            start_date = parse_date(start_date)
            end_date = parse_date(end_date)
            queryset = queryset.filter(date__range=[start_date, end_date])

        
        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset

    
    def create(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            task = serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError({"detail": "You already have a task with this title."})
        
        task_data = serializer.data
        event_data = {
            'title': task_data['title'],
            'description': task_data['description'],
            'start': f"{task_data['date']}T{task_data['time']}",
            'end': f"{task_data['date']}T{task_data['time_end']}",
        }

        try:
          
            event_result = create_google_calendar_event(event_data)            
            task.google_event_id = event_result.get('id', None)
            task.save()
            serializer = self.get_serializer(task)
        except Exception as e:
           
            return Response({
                "detail": "Error creating event in Google Calendar", 
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        
        


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        google_event_id = instance.google_event_id
        self.perform_destroy(instance)

        if google_event_id:
            try:
                delete_google_calendar_event(google_event_id)
            except Exception as e:
                
                return Response({"detail": "Erro ao deletar evento no Google Calendar", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_204_NO_CONTENT)




    
        