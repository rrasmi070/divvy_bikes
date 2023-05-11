from django.urls import include, path
from apis.views import *

urlpatterns = [
    path('total_docks_avail',Total_docks_avail.as_view(),name='total_docks_avail'),
    path('total_bikes_avail',Total_bikes_avail.as_view(),name='total_bikes_avail'),
    path('total_active_stations',Total_active_stations.as_view(),name='total_active_stations'),
    path('total_reserved_bike',Total_reserved_bike.as_view(),name='total_reserved_bike'),
    path('total_availables',Total_availables.as_view(),name='total_availables')
]