from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.forms import fields, widgets
from django.forms import formset_factory

# from django_select2 import forms as s2forms

from inventory import models as inv_models

# class Item_widget_s2form(s2forms.ModelSelect2Widget):
#     search_fields = [
#         "name__icontains",
#     ]

# My app imports
class Add_items_form(forms.ModelForm):
    class Meta:
        model = inv_models.Items
        fields = "__all__"
        exclude = ["store","shelf"]

class Add_request_form(forms.ModelForm):
    class Meta:
        model = inv_models.Request
        fields = "__all__"
        exclude = ["request_date", "approved_date", "status","approved_by"]
    
class Add_requestrow_form(forms.ModelForm):
    class Meta:
        model = inv_models.RequestRow
        fields = "__all__"
    
Add_requestrow_formset = formset_factory(Add_requestrow_form)
    
class Add_mesurement_form(forms.ModelForm):
    class Meta:
        model = inv_models.Measurement
        fields = "__all__"

class Add_category_form(forms.ModelForm):
    class Meta:
        model = inv_models.Category
        fields = "__all__"

class Add_store_form(forms.ModelForm):
    class Meta:
        model = inv_models.Store
        fields = "__all__"
        exclude = ["user"]
        
class Add_shelf_form(forms.ModelForm):
    class Meta:
        model = inv_models.Shelf
        fields = "__all__"
        widgets={"description":forms.Textarea(attrs={'required':'False'})}


class Update_item_form(forms.ModelForm):
    class Meta:
        model = inv_models.Items
        fields = "__all__"
        exclude = ["shelf","store"]

class Update_store_form(forms.ModelForm):
    class Meta:
        model = inv_models.Store
        fields = ["name","location","max_capacity"]

class Update_shelf_form(forms.ModelForm):
    class Meta:
        model = inv_models.Shelf
        fields = "__all__"

class Update_request_form(forms.ModelForm):
    class Meta:
        model = inv_models.Request
        fields = "__all__"
        # widgets={
        #     "store":Item_widget_s2form
        # }

class Test_form(forms.ModelForm):
    class Meta:
        model = inv_models.Propertys
        fields = "__all__"
        