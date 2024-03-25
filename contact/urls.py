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
    
    #USER
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.update_user_view, name='user_update'),
    
]
