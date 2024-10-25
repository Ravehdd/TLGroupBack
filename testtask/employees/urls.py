from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("api/v1/index/", Index.as_view()),
    path("api/v1/employee-data/", cache_page(600)(EmployeeAPIView.as_view())),
    path("api/v1/subdiv-role-data/", SubdivisionRolAPIView.as_view()),

]