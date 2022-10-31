from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductDetails
from django.contrib import messages
import csv,io

def product(request):
    if request.method =="POST":
        csvdata = request.FILES['file']
        if not csvdata.name.endswith('.csv'):
            messages.error(request,'This is not a csv file')
            return redirect('/')
        data_set=csvdata.read().decode('UTF-8')
        io_string=io.StringIO(data_set)
        next(io_string)

        for column in csv.reader(io_string,delimiter=',',quotechar="|"):
            save=Product.objects.create(
                name=column[0],
                price=column[1],
                purchase_date=column[2]
            )
        fm=Product.objects.all()
        messages.success(request,'File Successully Uploaded')

    else:
        fm=Product.objects.all()
    return render(request,'csv1/product.html',{'form':fm})




