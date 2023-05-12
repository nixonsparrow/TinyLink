from django.urls import path
from manager.views import LinkAPI

urlpatterns = [
    path("", LinkAPI.as_view(), name="links"),
    path("<str:short>/", LinkAPI.as_view(), name="link-redirect"),
]
