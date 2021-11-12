from typing import Counter
from django.db import models
import datetime

from django.db.models.aggregates import Count

# Create your models here.


class Product(models.Model):
    Name = models.CharField(max_length=100)
    
    
    def __str__(self) :
        return self.Name
    
    
class ProductSell(models.Model):
    Product=models.ForeignKey(to=Product , on_delete=models.PROTECT , verbose_name="product")
    Count=models.IntegerField()
    SellDateTime=models.DateField()
    
    monthdict={'January':'1' ,
               'February' : '1' ,
               'March' : '1',
               'April' : '1',
               'May': '1' ,
               'June' : '1',
               'July': '1' ,
               'August': '1' ,
               'September' : '1',
               'October' : '1',
               'November' : '1',
               'December': '1'}
    
    def __str__(self) -> str:
        return super().__str__()
    
    def get_month (self):
        return self.SellDateTime.strftime('%B')
    
    
    def get_report(self):
        prodects=Product.objects.all()
        result={}
        for k in self.monthdict.keys():
            plist=[]
            for i in range(0, prodects.count()):
                plist.append(0)
            result.update({k:plist})
        ct=0
        for product in prodects :
            productcells=ProductSell.objects.filter(Product_id=product.id)
            
            for ps in productcells :
                month=ps.get_month()
                count=ps.Count
                result[month][ct]=result[month][ct]+count
            ct+=1 
        return result           