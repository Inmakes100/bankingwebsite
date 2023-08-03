from .import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('new_page/',views.new_page,name='new_page'),
    path('form_page/',views.form_page,name='form_page'),
    path('logout/',views.logout,name='logout'),
    path('branches/',views.branches,name='branches'),
    path('wikipedia_redirect/',views.wikipedia_redirect,name='wikipedia_redirect'),

]
