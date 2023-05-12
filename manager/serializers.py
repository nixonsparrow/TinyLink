import random
from string import ascii_lowercase as letters
from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "short", "original", "created_at"]

    def create(self, validated_data):
        validated_data["short"] = self.generate_random_url()
        return super().create(validated_data)

    def generate_random_url(self, length=6):
        model = self.Meta.model
        random_url = ""
        while not random_url:
            random_url = "".join(random.choice(letters) for i in range(length))
            if model.objects.filter(short="random_url").exists():
                random_url = ""
        return random_url
