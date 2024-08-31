from user_app.models import Positions
from rest_framework import serializers


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = "__all__"

    id = serializers.CharField(read_only=True)

    def validate(self, data):
        name = data.get('name')
        if not name:
            raise serializers.ValidationError({"message": "Position name is required"})
        name = name.strip().lower()

        if Positions.objects.filter(name=name).exists():
            raise serializers.ValidationError({"message": "Position name already exists"})

        return data

    def create(self, validated_data):
        name = validated_data.get('name').lower().strip()
        return Positions.objects.create(name=name)

    def update(self, instance, validated_data):
        name = validated_data.get('name').lower().strip()
        instance.name = name
        instance.save()
        return instance
