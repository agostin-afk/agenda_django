from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    #CRUD
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    
    
    
]
