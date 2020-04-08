from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('scents/', views.scents_index, name='index'),
    path('scents/<int:scent_id>/', views.scents_detail, name='detail'),
    path('scents/<int:scent_id>/add_emotion',
         views.add_emotion, name='add_emotion'),
    # path('scents/<int:scent_id>/assoc_power/<int:power_id>/',
    #      views.assoc_power, name='assoc_power'),
    path('powers/', views.PowerList.as_view(), name='powers_index'),
    path('powers/<int:pk>/', views.PowerDetail.as_view(), name='powers_detail'),
    # path('powers/create/', views.PowerCreate.as_view(), name='powers_create'),
    path('powers/<int:pk>/update/',
         views.PowerUpdate.as_view(), name='powers_update'),
    path('powers/<int:pk>/delete/',
         views.PowerDelete.as_view(), name='powers_delete'),

]
