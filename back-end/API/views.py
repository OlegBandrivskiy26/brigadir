from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from DB_models.models import Talent, Contract, Project, User
from .serializer import (
    UserRegistrationSerializer, UserDetailSerializer, TalentSerializer,
    ProjectSerializer, ContractSerializer, UserLoginSerializer
)
from django.conf import settings

# Create your views here.

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"user": serializer.data, "token": token.key}, status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):  # Додаємо можливість оновлення профілю
        serializer = UserDetailSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_talent(request):
    serializer = TalentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # Update is_seller to True
        user = serializer.validated_data['user']
        user.is_seller = True
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("Validation errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_talent_by_id(request, talent_dsc_id):
    talents = Talent.objects.filter(talent_dsc_id=talent_dsc_id)
    serializer = TalentSerializer(talents, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("Validation errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_contract(request):
    serializer = ContractSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print("Validation errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_contract(request, contract_id):
    try:
        contract = Contract.objects.get(id=contract_id)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)
    except Contract.DoesNotExist:
        return Response({"error": "Contract not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    except Project.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_talents(request):
    talents = Talent.objects.filter(user=request.user)
    serializer = TalentSerializer(talents, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_projects(request):
    projects = Project.objects.filter(user_id=request.user)
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_contracts(request):
    contracts = Contract.objects.filter(user_id=request.user)
    serializer = ContractSerializer(contracts, many=True)
    return Response(serializer.data)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user_id=request.user)
    serializer = ProjectSerializer(project, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id, user_id=request.user)
    project.delete()
    return Response({"message": "Project deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_contract(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id, user_id=request.user)
    serializer = ContractSerializer(contract, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_contract(request, contract_id):
    contract = get_object_or_404(Contract, id=contract_id, user_id=request.user)
    contract.delete()
    return Response({"message": "Contract deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
