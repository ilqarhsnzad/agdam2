from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'backgound-colors', views.BackgroundColorViewSet, basename='background-color')
router.register(r'logos', views.LogoViewSet, basename='logo')
router.register(r'lights', views.LightViewSet, basename='light')
router.register(r'reklams', views.ReklamViewSet, basename='reklam')


urlpatterns = router.urls