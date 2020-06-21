from rest_framework import serializers
from .models import User
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username')

    def save(self):
        user_obj = User(email=self.validated_data['email'],
                        username=self.validated_data['username'],)
        user_obj.set_password(self.validated_data['password'])
        user_obj.save()
        return user_obj

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
