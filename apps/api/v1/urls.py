from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.test_example, name='example'),
]