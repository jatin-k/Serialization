from rest_framework import serializers
from snippets.models import NewUser

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    last_name = serializers.CharField()
    city = serializers.CharField()

    def create(self, validated_data):
        return NewUser.objects.create(**validated_data)