from rest_framework import serializers
from shan.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'dob',
                  'state', 'gender', 'location', 'pimage', 'rdoc']


class DummySerializer(serializers.Serializer):
    zipp = serializers.CharField(max_length=10)
    city = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=20)
    age = serializers.IntegerField()

    def __str__(self):
        return "Dummy Serializers Object"
