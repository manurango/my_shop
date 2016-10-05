from django.shortcuts import get_object_or_404, render
from chartit import DataPool, Chart
from .models import customer, category, product, purchase, purchase_item
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context,loader
from django.views.generic import TemplateView, ListView, DetailView
from django_tables2 import RequestConfig
from django.views import generic

class home_view(TemplateView):
    template_name = 'shop/home.html'
    
    def get_context_data(self, **kwargs):
         context = super(home_view, self).get_context_data(**kwargs)
         #context['my_orders'] = customer_order.objects.all()
         context['products'] = product.objects.order_by('date')[:12]
         return context

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            my_product = product.objects.filter(product_name__icontains=q)
        return render(request, 'search_results.html',
                {'my_product': my_product, 'query': q})
    return render(request, 'home.html',
        {'errors': errors})


class product_view(TemplateView):
    template_name = 'shop/product.html'
    
    def get_context_data(self, **kwargs):
         context = super(product_view, self).get_context_data(**kwargs)
         #context['my_orders'] = customer_order.objects.all()
         context['my_products'] = product.objects.all()
         return context


'''class product_detail_view(generic.DetailView):
    model = product
    template_name = 'shop/product-detail.html'
'''
class purchase_item_view(TemplateView):
    template_name = 'shop/purchases.html'

    def get_ds(self):
        return DataPool(
            series=[{'options': {
                'source': purchase_item.objects.all()},
                'terms': [
                'purchase_date',
                'product_id',
                #'product_category',
                'price',
                'quantity',
                'total_price']}
             ])

    def get_order_chart(self):
        return Chart(
            datasource=self.get_ds(),
            series_options=[{'options':{
                  'type': 'bar',
                  'stacking': False},
                'terms':{
                  'purchase_date': [
                    'product_id',
                #'product_category',
                'price',
                'quantity',
                    'total_price',
                    ]}}],
            chart_options={'title': {
                'text': 'Purchases Chart & Table '},
                'xAxis': {
                'title': {
                    'text': 'date'}}})

    def get_context_data(self, **kwargs):
        context = super(purchase_item_view, self).get_context_data(**kwargs)
        context['my_orders'] = purchase_item.objects.order_by('-purchase_date')[:7]
        context['my_tables'] = purchase_item.objects.order_by('-purchase_date')[:10]
        context['orderchart'] = self.get_order_chart()

        return context
# Create your views here.
