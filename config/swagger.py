# config/swagger.py
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Intern-Log API Documentation",
        default_version='v1',
        description="API documentation for the Intern-Log Application",
        terms_of_service="",
        contact=openapi.Contact(email="akumbomwesley802@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)