from rest_framework import serializers
from DB_models.models import User, Talent, Contract, Project

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'age', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True},  # Пароль приховуємо
            'phone_number': {'required': False, 'allow_null': True}
        }

    def create(self, validated_data):
        validated_data.pop('username', None)  # Видаляємо username, якщо він є
        user = User.objects.create_user(**validated_data)
        return user



class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'age', 'phone_number', 'is_seller']


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
