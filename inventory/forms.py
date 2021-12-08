from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.forms import fields, widgets

from inventory import models as inv_models

# My app imports
class Add_items_form(forms.ModelForm):
    class Meta:
        model = inv_models.Items
        fields = "__all__"
        exclude = ["store","shelf"]
class Add_mesurement_form(forms.ModelForm):
    class Meta:
        model = inv_models.Measurement
        fields = "__all__"

class Add_catagory_form(forms.ModelForm):
    class Meta:
        model = inv_models.Catagory
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
        

# class EmployeeContactUpdate(forms.Form):
#     contactFirstName =  forms.CharField(label = "First Name", required=False)
#     contactLastName =  forms.CharField(label = "Last Name", required=False)
#     contactCountry = forms.CharField(label="Country", required=False)
#     contactRegion = forms.CharField(label="Region", required=False)
#     contactKebele = forms.CharField(label="Kebele", required=False)
#     contactGovernmentId = forms.FileField(label="Government Issued Id", required=False)
#     contactZone = forms.CharField(label="Zone", required=False)
#     contactWereda = forms.CharField(label="Wereda", required=False)
#     contactPhone = forms.CharField(label="Phone Number", required=False)

# class EmployeeTerminateForm(forms.ModelForm):
#     class Meta:
#         model = EmployeeTermination
#         exclude = ["employee", "dateOfTermination", "idReturn", "isCleared", "status"]
#         widgets = {
#             "reason": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                     "rows": "5",
#                     "spellcheck": "true",
#                     "placeholder": "State reason here",
#                 }
#             ),
#         }

# class EmployeeGetForm(forms.ModelForm):
#     class Meta:
#         model = EmployeeTermination
#         fields = ['employee']
#         widgets = {
#             'employee':forms.Select(attrs={'class': 'mb-3 form-control',}),
#         }

# class UserAddForm(forms.ModelForm):
#     class Meta:
#         model = User
#         exclude = ["user_permissions","first_name","last_name",'is_superuser','is_staff',"email","date_joined","last_login","is_active"]

#         widgets={
#             'username':forms.TextInput(attrs={'class': 'mb-3 form-control', 'placeholder':'Enter username'}),
#             'password':forms.TextInput(attrs={'class': 'mb-3 form-control', 'type':"password",'placeholder':'Password'}),
#             # 'is_superuser':forms.CheckboxInput(attrs={"style":"padding-right:20px; margin-right:20px; line-break: auto ;",'placeholder':'Is Superuser'}),
#             # 'is_staff':forms.CheckboxInput(attrs={"style":"padding-right:20px; margin-right:20px;", 'placeholder':'Is Staff'}),
#             'groups':forms.Select(attrs={'class': 'mb-3 form-control'}),
#         }
    