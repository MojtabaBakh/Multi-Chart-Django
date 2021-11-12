from django.shortcuts import render
from .models import Product ,  ProductSell 
from json import dumps


# Create your views here.

def index_view(request):
    productsell=ProductSell()
    result=productsell.get_report()
    datajson=dumps(result)
    print(datajson)
    context={  
             'result': datajson ,
            }
    
    return render(request , "dashboard/index.html" , context )
    