from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# router = DefaultRouter()
# router.register(r"register", RegisterView, basename="register")
# router.register(r"login", LoginView, basename="login")

# urlpatterns = router.urls
urlpatterns = [
    path("register", RegisterView.as_view()),
    path("login", LoginView.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("", include(router.urls))
]
