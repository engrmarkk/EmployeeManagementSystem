from rest_framework.routers import SimpleRouter
from .views import PositionView
from django.urls import path, include

router = SimpleRouter()
router.register(r"position", PositionView, basename="position")

# urlpatterns = router.urls
urlpatterns = [
    path("", include(router.urls))
]
