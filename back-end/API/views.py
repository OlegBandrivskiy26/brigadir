from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from DB_models.models import Talent, Contract, Project, Talent_dsc
from .serializer import UserRegistrationSerializer, UserDetailSerializer, TalentSerializer, ProjectSerializer, \
    ContractSerializer

# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserDetailSerializer(request.user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_talent(request):
    data = request.data.copy()
    data['user'] = request.user.id  # автоматично встановлюємо користувача

    serializer = TalentSerializer(data=data)
    if serializer.is_valid():
        talent = serializer.save()

        request.user.is_seller = True
        request.user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_talent_by_id(request, talent_dsc_id):
    talents = Talent.objects.filter(talent_dsc_id=talent_dsc_id)

    # If you only expect one result, you can return the first one
    if talents.exists():
        serializer = TalentSerializer(talents, many=True)
        return Response(serializer.data)
    else:
        return Response({"detail": "Talent not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_talent_dsc_list(request):
    talent_dscs = Talent_dsc.objects.all().order_by('prof')  # Example of sorting by profession name
    data = [{"id": t.id, "prof": t.prof} for t in talent_dscs]
    return Response(data)


@api_view(['POST'])
def create_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_contract(request):
    serializer = ContractSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
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
