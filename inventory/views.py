from json.encoder import JSONEncoder
from django.db import models
from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render
from django.utils.translation import templatize
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.views.generic.detail import SingleObjectMixin
from inventory import models as inv_models
from inventory import forms as inv_forms
from authentications import models as auth_models
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ home page ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
class Home(LoginRequiredMixin, TemplateView ):
    template_name = "inventory/Home.html"


#  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ test classes ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
class Test(LoginRequiredMixin, TemplateView):
    template_name = "pages/table.html"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ add and list items ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
class Add_items(LoginRequiredMixin, CreateView):
    model = inv_models.Items
    form_class = inv_forms.Add_items_form
    template_name = "inventory/item/add_item.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"catagories":inv_models.Catagory.objects.all()})
        return context

    def get_success_url(self):
        return reverse_lazy('Add_placement_value', args=(self.object.id,))


class Add_placement_value(LoginRequiredMixin, TemplateView):
    model = inv_models.Items
    form_class = inv_forms.Add_items_form
    template_name = "inventory/item/add_item_placement.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "stores":inv_models.Store.objects.all(),
            "shelfs":inv_models.Shelf.objects.all(),
        })
        return context
    
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        item = inv_models.Items.objects.get(id=kwargs['pk'])
        item.store = inv_models.Store.objects.get( id = request.POST.get('store'))
        item.shelf = inv_models.Shelf.objects.get(id = request.POST.get('shelf'))
        item.save()
        return redirect(reverse_lazy('Add_measurement_value', args=(kwargs['pk'],)))


class Add_measurement_value(LoginRequiredMixin, ListView):
    model = inv_models.Items
    # form_class = inv_forms.Add_items_form
    template_name = "inventory/item/list_item.html"
    # success_url = reverse_lazy("List_items")
    
class List_items(LoginRequiredMixin, ListView):
    template_name = "inventory/item/list_item.html"
    model = inv_models.Items

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ add and list measurement ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
class Add_measurements(LoginRequiredMixin, CreateView):
    model = inv_models.Measurement
    form_class = inv_forms.Add_mesurement_form
    template_name = "inventory/measurement/add_measurement.html"
    success_url = reverse_lazy("List_measurements")

class List_measurements(LoginRequiredMixin, ListView):
    model = inv_models.Measurement
    template_name = "inventory/measurement/list_measurement.html"


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ add and list measurement ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
class Add_catagories(LoginRequiredMixin, CreateView):
    model = inv_models.Catagory
    form_class = inv_forms.Add_catagory_form
    template_name = "inventory/catagory/add_catagory.html"
    success_url = reverse_lazy("List_catagories")

    
class List_catagories(LoginRequiredMixin, ListView):
    model = inv_models.Catagory
    template_name = "inventory/catagory/list_catagory.html"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ add and list store ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
class Add_store(LoginRequiredMixin, CreateView):
    model = inv_models.Store
    form_class = inv_forms.Add_store_form
    template_name = "inventory/store/add_store.html"

    def form_valid(self, form):
        store = inv_models.Store(name = form.cleaned_data["name"], location = form.cleaned_data["location"], 
            user = self.request.user,max_capacity=form.cleaned_data["max_capacity"])
        store.save()

        return redirect (reverse_lazy("List_store"))


class List_store(LoginRequiredMixin, ListView):
    model = inv_models.Store
    template_name = "inventory/store/list_store.html"

    
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ add and list shelf ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
class Add_shelf(LoginRequiredMixin, CreateView):
    model = inv_models.Shelf
    form_class = inv_forms.Add_shelf_form
    template_name = "inventory/shelf/add_shelf.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'stores': inv_models.Store.objects.all()})
        return context
    
    def form_valid(self, form):
        shelfs_count = len(inv_models.Shelf.objects.filter(store=form.cleaned_data["store"]))
        if(shelfs_count < form.cleaned_data["store"].max_capacity): 
            shelf = inv_models.Shelf(name=form.cleaned_data["name"],store=form.cleaned_data["store"],
                description=form.cleaned_data["description"],max_capacity=form.cleaned_data["max_capacity"])
            shelf.save()

            return redirect(reverse_lazy("List_shelf"))
        else:
            return redirect(reverse_lazy("Capacity_error"))
        
        
class List_shelf(LoginRequiredMixin, ListView):
    model = inv_models.Shelf
    template_name = "inventory/shelf/list_shelf.html"

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ Errors ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Capacity_error(LoginRequiredMixin, TemplateView):
    template_name = "inventory/capacity_error.html"