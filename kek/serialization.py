from rest_framework import serializers
from .models import User
class reg_seria(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def create(self, validated_data):
        return User.objects.create(**validated_data)
class auth_seria(serializers.Serializer):
    login_user = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=41)
    # print(login,password)
    def check(self,validated_data):
        User.objects.get(pk =validated_data.login_user)
        User.objects.get(password=validated_data.password)
        # return User.objects.get(pk =validated_data.login)