from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name=""),
    path('application/submit/', views.submit, name="submit"),
    path('/application/', views.application, name="application"),
    ]