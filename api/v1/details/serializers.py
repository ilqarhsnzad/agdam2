from rest_framework import serializers
from details.models import BackgroundColor, Logo, Light, Reklam

class BackgroundColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundColor
        fields = "__all__"


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"


class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = "__all__"


class ReklamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reklam
        fields = "__all__"