from rest_framework import serializers
from .models import TODOIList,Login

class TODOIListSerializer(serializers.ModelSerializer):
    class Meta:
        model=TODOIList 
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login 
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login 
        fields = 'FirstName','LastName','Email','IsActive','Roles'