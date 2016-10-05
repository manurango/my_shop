import django_tables2 as tables
form .models import purchase_item

class purchase_table(tables.Table):
    purchase_date = tables.Column(verbose_name='Date')
    purchase_id = tables.Column(verbose_name='Purcahse Id')
    price = tables.Column(verbose_name='Price per Unit')
    quantity = tables.Column(verbose_name='Quantity')
    total_price = tables.Column(verbose_name='Totals')

    class Meta:
        model = purchase_item
        attrs = {"class":"paleblue"}
    
