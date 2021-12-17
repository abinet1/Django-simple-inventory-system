
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views as inventory_views
# from dal import autocomplete
# from django.conf.urls import url
# from inventory import models as inv_models

urlpatterns = [
    # url('test-autocomplete/$',autocomplete.Select2QuerySetView.as_view(model=inv_models.RequestRow),name='select2_fk',),
    path('', inventory_views.Home.as_view(), name="Home"),
    
    path('form/', inventory_views.Test.as_view(), name="Test"),
    
    path('item/add/', inventory_views.Add_items.as_view(), name="Add_items"),
    path('item/add/placement/<int:pk>', inventory_views.Add_placement_value.as_view(), name="Add_placement_value"),
    path('item/add/measurement/<int:pk>', inventory_views.Add_measurement_value.as_view(), name="Add_measurement_value"),
    path('item/list/', inventory_views.List_items.as_view(), name="List_items"),
    path('item/update/<int:pk>', inventory_views.Update_item.as_view(), name="Update_item"),
    path('item/detail/<int:pk>', inventory_views.Detail_item.as_view(), name="Detail_item"),
    
    path('measurement/add/', inventory_views.Add_measurements.as_view(), name="Add_measurements"),
    path('measurement/list/', inventory_views.List_measurements.as_view(), name="List_measurements"),

    path('shelf/add/', inventory_views.Add_shelf.as_view(), name="Add_shelf"),
    path('shelf/list/', inventory_views.List_shelf.as_view(), name="List_shelf"),
    path('shelf/update/<int:pk>/', inventory_views.Update_shelf.as_view(), name="Update_shelf"),
    path('shelf/detail/<int:pk>/', inventory_views.Detail_shelf.as_view(), name="Detail_shelf"),
    
    path('request/add/', inventory_views.Add_request.as_view(), name="Add_request"),
    path('request/list/', inventory_views.List_request.as_view(), name="List_request"),
    path('request/detail/<int:pk>/', inventory_views.Detail_request.as_view(), name="Detail_request"),#inventory_views.Detail_request ->on going
    path('request/update/<int:pk>/', inventory_views.Update_request.as_view(), name="Update_request"),#inventory_views.Update_request ->on going 
    path('request/approve/<int:pk>/', inventory_views.Approve_request.as_view(), name="Approve_request"),

    path('store/add/', inventory_views.Add_store.as_view(), name="Add_store"),
    path('store/list/', inventory_views.List_store.as_view(), name="List_store"),
    path('store/detail/<int:pk>/', inventory_views.Detail_store.as_view(), name="Detail_store"),
    path('store/update/<int:pk>/', inventory_views.Update_store.as_view(), name="Update_store"),  
    
    path('error/capacity_error',inventory_views.Capacity_error.as_view(), name="Capacity_error"),
    
    path('categories/add/', inventory_views.Add_categories.as_view(), name="Add_categories"),
    path('categories/list/', inventory_views.List_categories.as_view(), name="List_categories"),
    path('categories/detail/<int:pk>/', inventory_views.Detail_category.as_view(), name="Detail_category"),
    path('categories/update/<int:pk>/', inventory_views.Update_category.as_view(), name="Update_category")
]