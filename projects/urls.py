from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.projectsmain, name='projectsmain'),
    path('<int:project.id>/', views.project_detail, name='project_detail'),
]
