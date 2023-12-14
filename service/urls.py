from django.urls import path
from . import views

urlpatterns = [
        path('', views.services,name='services'),
        path('<str:pk>', views.service,name='service'),
        path('feedback/', views.feedback_form,name='feedback'),

]