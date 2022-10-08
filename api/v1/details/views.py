from . import serializers
from details.models import BackgroundColor,Light,Logo,Reklam
from rest_framework.viewsets import ModelViewSet
from .. import permissions as my_permission


class BackgroundColorViewSet(ModelViewSet):
    serializer_class = serializers.BackgroundColorSerializer
    queryset = BackgroundColor.objects.all()
    permission_classes = [my_permission.IsAdminUserOrReadOnly]


class LightViewSet(ModelViewSet):
    serializer_class = serializers.LightSerializer
    queryset = Light.objects.all()
    

class LogoViewSet(ModelViewSet):
    serializer_class = serializers.LogoSerializer
    queryset = Logo.objects.all()
    permission_classes = [my_permission.IsAdminUserOrReadOnly]


class ReklamViewSet(ModelViewSet):
    serializer_class = serializers.ReklamSerializer
    queryset = Reklam.objects.all()
    permission_classes = [my_permission.IsAdminUserOrReadOnly]