from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('scents/', views.scents_index, name='index'),
    path('scents/<int:scent_id>/', views.scents_detail, name='detail'),
    path('scents/<int:scent_id>/add_emotion',
         views.add_emotion, name='add_emotion')
]
