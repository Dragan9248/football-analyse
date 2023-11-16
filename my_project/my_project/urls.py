"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('teams/', views.team_list, name='team_list'),  # Список команд
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),  # Детали команды по идентификатору (pk)
    path('players/', views.player_list, name='player_list'),  # Список игроков
    path('players/<int:pk>/', views.player_detail, name='player_detail'),  # Детали игрока по идентификатору (pk)
    path('matches/', views.match_list, name='match_list'),  # Список матчей
    path('matches/<int:pk>/', views.match_detail, name='match_detail'),  # Детали матча по идентификатору (pk)
]
