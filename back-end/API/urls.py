from django.urls import path
from .views import (
    UserRegistrationView, add_talent, get_talent_by_id, create_project,
    create_contract, get_contract, get_project, UserLoginView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('add_talent/', add_talent, name='add_talent'),
    path('talent/<int:talent_dsc_id>/', get_talent_by_id, name='get_talent_by_id'),
    path('create_project/', create_project, name='create_project'),
    path('create_contract/', create_contract, name='create_contract'),
    path('contract/<int:contract_id>/', get_contract, name='get_contract'),
    path('project/<int:project_id>/', get_project, name='get_project'),
    path("login/", UserLoginView, name="login"),
]
