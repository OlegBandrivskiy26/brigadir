from rest_framework import serializers
from DB_models.models import User, Talent, Contract, Project


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'age', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}  # Пароль приховуємо
        }

    def create(self, validated_data):
        # Створення користувача з хешованим паролем
        user = User.objects.create_user(**validated_data)
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'age', 'phone_number', 'is_seller']


class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = ['user', 'position', 'description', 'location', 'talent_dsc']

class UpdateSellerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_seller']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
