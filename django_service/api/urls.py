from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import ProtectedView

urlpatterns = [
    path("gen-token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("protected-data/", ProtectedView.as_view(), name="protected_data"),
]
