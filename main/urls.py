from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import RegistrationViews, AllStatements, CreateStatement


urlpatterns = [
    path('', RegistrationViews.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', AllStatements, name='profile'),
    path('create/', CreateStatement, name='create'),
    path('statements/', views.statement_list, name='statement_list'),
    path('accept/<int:statement_id>/', views.accept_statement, name='accept_statement'),
    path('reject/<int:statement_id>/', views.reject_statement, name='reject_statement'),
]