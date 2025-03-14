from django.urls import path
from .views import (
    UserRegistrationView, add_talent, get_talent_by_id, create_project,
    create_contract, get_contract, get_project, UserLoginView,
    UserDetailView, get_user_talents, get_user_projects, get_user_contracts,
    update_project, delete_project, update_contract, delete_contract
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('add_talent/', add_talent, name='add_talent'),
    path('talent/<int:talent_dsc_id>/', get_talent_by_id, name='get_talent_by_id'),
    path('create_project/', create_project, name='create_project'),
    path('create_contract/', create_contract, name='create_contract'),
    path('contract/<int:contract_id>/', get_contract, name='get_contract'),
    path('project/<int:project_id>/', get_project, name='get_project'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('users/me/', UserDetailView.as_view(), name='user_detail'),
    path('users/me/talents/', get_user_talents, name='user_talents'),
    path('users/me/projects/', get_user_projects, name='user_projects'),
    path('users/me/contracts/', get_user_contracts, name='user_contracts'),
    path('project/<int:project_id>/update/', update_project, name='update_project'),
    path('project/<int:project_id>/delete/', delete_project, name='delete_project'),
    path('contract/<int:contract_id>/update/', update_contract, name='update_contract'),
    path('contract/<int:contract_id>/delete/', delete_contract, name='delete_contract'),
]
