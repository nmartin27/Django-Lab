from django.urls import path
from . import views

urlpatterns = [
    path('api/company', views.CompanyList.as_view(), name = 'company_list'),
    path('api/company/<int:pk>', views.CompanyDetail.as_view(), name = 'company_detail'),
]

urlpatterns = [
    path('api/location', views.LocationList.as_view(), name = 'location_list'),
    path('api/location/<int:pk>', views.LocationDetail.as_view(), name = 'location_detail'),
]