from companies.urls import companies_router
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path("admin/", admin.site.urls),
  path("", include(companies_router.urls))
]
