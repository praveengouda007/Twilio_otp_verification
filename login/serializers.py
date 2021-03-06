from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'is_superuser', 'phone']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    # def update(self, instance, validate_data):
    #     instance.phone = validate_data.get('phone', instance.phone)
    #     instance.save()
    #     return instance


# class VerifySerializer(serializers.ModelSerializer):
#     code = serializers.CharField(max_length=8, required=True)
