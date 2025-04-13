from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from DB_models.models import Talent_dsc
from .authentication import CustomTokenObtainPairView
from .views import (
    UserRegistrationView, add_talent, get_talent_by_id, create_project,
    create_contract, get_contract, get_project, UserDetailView, get_talent_dsc_list, get_projects
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('add_talent/', add_talent, name='add_talent'),
    path('talent/<int:talent_dsc_id>/', get_talent_by_id, name='get_talent_by_id'),
    path('create_project/', create_project, name='create_project'),
    path('create_contract/', create_contract, name='create_contract'),
    path('contract/<int:contract_id>/', get_contract, name='get_contract'),
    path('project/<int:project_id>/', get_project, name='get_project'),
    path('login/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('talent_dsc/', get_talent_dsc_list, name='talent_dsc'),
    path('me/', UserDetailView.as_view(), name='user_detail'),
    path('projects_list/', get_projects, name='projects_list'),
]
