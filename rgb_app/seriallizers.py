from rest_framework import serializers

from rgb_app.models import Chemical_Properties

class chemical_value_serializer(serializers.ModelSerializer):
    class Meta:
        model=Chemical_Properties
        fields='__all__'
