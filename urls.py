from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:ticket_id>/', views.detail, name='Ticket detail')
]
