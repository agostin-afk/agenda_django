from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('contatc/<int:contact_id>/detail/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    #CRUD
    path('contatc/create/', views.create, name='create'),
    path('contatc/<int:contact_id>/delete/', views.contact, name='contact'),
    path('contatc/<int:contact_id>/update/', views.contact, name='contact'),
    
    
    
]
