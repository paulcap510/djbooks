from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_results/', views.search_results, name='search_results'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),    
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
]
