from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Company

from .serializers import CompanySerializer

# Create your views here.
class CompanyViewsSet(ModelViewSet):
  serializers_class = CompanySerializer
  queryset = Company.objects.all().order_by('-last_update')
