from rest_framework import serializers

from reconciliation.models import Work
from .contributor import ContributorSerializer


class WorkSerializer(serializers.ModelSerializer):

    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Work
        fields = '__all__'
