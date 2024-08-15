from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

#serializer for user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ProjectName(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [ 'project_name']

#serializer for Client model
class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField() 
    projects = ProjectName(many=True, read_only=True) 
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects','created_at', 'updated_at', 'created_by']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()  
    users = UserSerializer(many=True) 

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

# Serializer for project 
class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    
    class Meta:
        model = Project
        fields = ['project_name', 'client', 'users']

    # Override create assign user
    def create(self, validated_data):
        users = validated_data.pop('users')  
        project = Project.objects.create(**validated_data)  
        project.users.set(users)  
        return project
