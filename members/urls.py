from django.urls import path
from django.contrib import admin
from.import views

urlpatterns = [
     
    path('home',views.home, name='home'),
    path('details', views.details,name='details'),
    path('field', views.field,name='field'),
    path('addmoredetails', views.addMoredetail,name='addmoredetails'),
    path('edit', views.edit,name='edit'),
    path('updatesave',views.updatesave,name='updatesave'),
    path('',views.login_view,name='login_view'),
    # path('logout_view',views.logout_view,name='logout_view'),
    
]