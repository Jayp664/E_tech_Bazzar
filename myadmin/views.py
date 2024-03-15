from django.shortcuts import render

# Create your views here.
def layout(request):
    contex = {}
    return render(request,'myadmin/layout.html',contex)

def dash(request):
    contex = {}
    return render(request,'myadmin/dash.html',contex)

def common_form(request):
    contex = {}
    return render(request,'myadmin/common_form.html',contex)

def add_categories(request):
    contex = {}
    return render(request, 'myadmin/add_cat.html',contex)


def add_subcat(request):
    contex = {}
    return render(request, 'myadmin/add_subcat.html',contex)


def common_table(request):
    contex = {}
    return render(request, 'myadmin/common_table.html',contex)


def all_cat(request):
    contex = {}
    return render(request, 'myadmin/all_cat.html',contex)


def all_subcat(request):
    contex = {}
    return render(request, 'myadmin/all_subcat.html',contex)

def view_customer(request):
    contex = {}
    return render(request,'myadmin/view_customer.html',contex)


def view_order(request):
    contex = {}
    return render(request,'myadmin/view_order.html',contex)

def payment(request):
    contex = {}
    return render(request,'myadmin/payment.html',contex)

def signin(request):
    contex = {}
    return render(request,'myadmin/signin.html',contex)