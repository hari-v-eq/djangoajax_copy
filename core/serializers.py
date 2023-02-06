from rest_framework import serializers
from core.models import Student

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model= Student
        # fields="__all__"
        fields = ['id','name','email','course']