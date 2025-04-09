from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'https://potential-adventure-wgvpg46jprpc9wp-8000.app.github.dev/api/users/',
        'teams': 'https://potential-adventure-wgvpg46jprpc9wp-8000.app.github.dev/api/teams/',
        'activities': 'https://potential-adventure-wgvpg46jprpc9wp-8000.app.github.dev/api/activities/',
        'leaderboard': 'https://potential-adventure-wgvpg46jprpc9wp-8000.app.github.dev/api/leaderboard/',
        'workouts': 'https://potential-adventure-wgvpg46jprpc9wp-8000.app.github.dev/api/workouts/'
    })

def api_endpoint(request):
    return JsonResponse({
        "message": "Welcome to OctoFit API!",
        "url": "https://potential-adventure-wgvpg46jprpc9wp-8000.app.github.dev"
    })

def another_endpoint(request):
    return JsonResponse({
        "info": "This is another endpoint.",
        "url": "https://potential-adventure-wgvpg46jprpc9wp-8000.app.github.dev"
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer