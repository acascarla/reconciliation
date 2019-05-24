from rest_framework import serializers

from reconciliation.models import Contributor


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
