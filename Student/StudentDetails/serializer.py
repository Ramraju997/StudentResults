from rest_framework import serializers
from StudentDetails.models import Students


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id',
                  'name',
                  'rollnumber',
                  'dateofbirth',
                  'marks')