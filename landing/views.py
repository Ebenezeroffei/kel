from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from django.views import View,generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product


# Create your views here.

class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'landing/index.html'
    
    def get_context_data(self,*args,**kwargs):
        """ This method adds another key to the dictionary that will show if an item which is being displayed is already in the user's cart """
        context = super().get_context_data(*args,**kwargs)
        if self.request.user.is_authenticated:
            added_items = [pro for pro in  Product.objects.all() for item in self.request.user.usercartitems_set.all() if pro.product_name == item.item_name ]
            context['added_items'] = added_items
            
        return context
    
class ProductDetailView(generic.DetailView):
    model = Product
    
    def get_context_data(self,*args,**kwargs):
        # Get the context data
        context = super().get_context_data(*args,**kwargs)
        if self.request.user.is_authenticated:
            added_items = [pro for pro in  Product.objects.all() for item in self.request.user.usercartitems_set.all() if pro.product_name == item.item_name ]
            context['added_items'] = added_items
        # Get the product beign showed
        product_id = int(self.kwargs.get('pk'))
        other_products = Product.objects.exclude(id = product_id)
        context["other_products"] = other_products
        return context
    
class AddItemsToCartView(View):
    def get(self,request,*args,**kwargs):
        """ This method adds an item to a userscart """
        # Use the id of the product to get the product
        product_id = int(request.GET.get('product_id',None))
        product = get_object_or_404(Product,id = product_id)
        # Add product to the user's cart
        request.user.usercartitems_set.create(item_name = product.product_name)
        data = {
                'total_basket_items':request.user.usercartitems_set.count(),
        }
        
        return JsonResponse(data)

    
class ItemsSearchView(generic.ListView):
    """ This class returns the search results """
    model = Product
    template_name = 'landing/search_results.html'
    
    def get_context_data(self,*args,**kwargs):
        results = self.request.GET.get("q");
        context = super().get_context_data(*args,**kwargs)
        context['results'] = Product.objects.filter(product_name__icontains = results)
        if self.request.user.is_authenticated:
            added_items = [pro for pro in  Product.objects.all() for item in self.request.user.usercartitems_set.all() if pro.product_name == item.item_name ]
            context['added_items'] = added_items
        print(context['results'])
        return context
