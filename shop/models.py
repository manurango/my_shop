from django.db import models

class customer(models.Model):
    date_joined = models.DateField(auto_now=True)
    name = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.name
    class Meta:
        ordering = ['-date_joined']

class category(models.Model):
    category_name = models.CharField(max_length=20)
    other_details = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return "%s" % self.category_name

class product(models.Model):
    date = models.DateField(auto_now=True)
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to='images/')
    price = models.FloatField(default=0)
    product_category = models.ForeignKey(category)

    def __str__(self):
        return "%s @Ksh- %s" % (self.product_name, self.price)
    
class purchase(models.Model):
    date = models.DateTimeField(auto_now=True)
    customer_id = models.ForeignKey(customer)

    class Meta:
        ordering = ['-date']
    

    def __str__(self):
        return "P.Id: %s -Name: %s" % ( self.pk, self.customer_id)


class purchase_item(models.Model):
    purchase_date= models.DateField()
    purchase_id = models.ForeignKey(purchase)
    product_id = models.ForeignKey(product)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.total_price= self.price*self.quantity
        super(purchase_item, self).save(*args, **kwargs)

    def __str__(self):
        return "%s %s" % (self.product_id, self.total_price)

    

# Create your models here.
