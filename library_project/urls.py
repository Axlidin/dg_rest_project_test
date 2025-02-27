from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Book Library API",
        default_version='v1',
        description="API for managing books",
        terms_of_service="demo version",
        contact=openapi.Contact(email="akhlidinshermatov00@gmail.com"),
        license=openapi.License(name="currnetly free"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),

    #swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #redoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
