from django.contrib import admin
from django.urls import path
from core import views




urlpatterns= [

    path('home/',views.home, name='home'),
    path('save/', views.save_data, name='save'),
    path('delete/', views.delete_data, name='delete'),
    path('edit/', views.edit_data, name='edit'),
    path('search/',views.searchbar, name='searchbar'),
    path('api/',views.ItemViews.as_view()),
    path('api/<int:id>/',views.ItemViews.as_view())
   
]

