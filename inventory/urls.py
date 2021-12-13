
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views as inventory_views

urlpatterns = [
    path('', inventory_views.Home.as_view(), name="Home"),
    
    path('form/', inventory_views.Test.as_view(), name="Test"),
    
    path('item/add/', inventory_views.Add_items.as_view(), name="Add_items"),
    path('item/add/placement/<int:pk>', inventory_views.Add_placement_value.as_view(), name="Add_placement_value"),
    path('item/add/measurement/<int:pk>', inventory_views.Add_measurement_value.as_view(), name="Add_measurement_value"),
    path('item/list/', inventory_views.List_items.as_view(), name="List_items"),
    
    path('measurement/add/', inventory_views.Add_measurements.as_view(), name="Add_measurements"),
    path('measurement/list/', inventory_views.List_measurements.as_view(), name="List_measurements"),
    
    path('shelf/add/', inventory_views.Add_shelf.as_view(), name="Add_shelf"),
    path('shelf/list/', inventory_views.List_shelf.as_view(), name="List_shelf"),    
    
    path('request/add/', inventory_views.Add_request.as_view(), name="Add_request"),
    path('request/list/', inventory_views.List_request.as_view(), name="List_request"),

    path('store/add/', inventory_views.Add_store.as_view(), name="Add_store"),
    path('store/list/', inventory_views.List_store.as_view(), name="List_store"),    
    
    path('error/capacity_error',inventory_views.Capacity_error.as_view(), name="Capacity_error"),
    
    path('catagories/add/', inventory_views.Add_catagories.as_view(), name="Add_catagories"),
    path('catagories/list/', inventory_views.List_catagories.as_view(), name="List_catagories"),
]