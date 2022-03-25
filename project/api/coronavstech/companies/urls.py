from rest_framework import routers

from .views import CompanyViewsSet

companies_router = routers.DefaultRouter()
companies_router.register("companies", viewset=CompanyViewsSet, basename="companies")
