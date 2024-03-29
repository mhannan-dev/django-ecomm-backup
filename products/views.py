from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.

class ProductFeaturedListView(ListView):
    template_name = "products/product_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/feature_detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()




class ProductListView(ListView):
    #queryset = Product.objects.all()
    template_name = "products/product_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()

    context ={
            'object_list':queryset
    }
    return render(request,"products/product_list.html",context)

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/product_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist")
        return instance
    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)





def product_detail_view(request, pk=None, *args, **kwargs):

    # instance = Product.objects.get(pk=pk, featured=True)
    # instance = get_object_or_404(Product, pk=pk, featured=True)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('No product here')
    #     raise Http404("Product does not exist")
    #     print("Huh?")
    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product does not exist")

    # print(instance)
    #
    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product does not exist")



    # queryset = Product.objects.all()

    context ={
            'object':instance
    }
    return render(request,"products/product_detail.html",context)


