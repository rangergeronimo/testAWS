from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.chart, name='chart'),
    path('sensor/', views.sensor, name='sensor')
]
