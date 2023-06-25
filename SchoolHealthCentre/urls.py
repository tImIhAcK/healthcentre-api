from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="DLCF API",
      default_version='v1',
      description="Restful Implementation of School Health Centre API",
      contact=openapi.Contact(email="adeniranjohn2016@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(
        r"^$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="dlcf_api_docs",
    ),
        
    path("admin/", admin.site.urls),
    path('api/v1/healthcentre/', include('HealthCentre.urls'))
]
