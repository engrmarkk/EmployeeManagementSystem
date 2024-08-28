from rest_framework.routers import DefaultRouter
from .views import AuthAppViewSet

router = DefaultRouter()
router.register(r"register", AuthAppViewSet, basename="register")

urlpatterns = router.urls
