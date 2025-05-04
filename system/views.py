from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse , HttpResponseRedirect
from django.db.models import Q

from .models import House, Order, PrivateMsg
from .forms import HouseForm, OrderForm, MessageForm
from django.contrib import messages
import requests




def home(request):
    context = {
        "title" : "House Rental"
    }
    return render(request,'home.html', context)

def house_list(request):
    house = House.objects.all()

    query = request.GET.get('q')
    if query:
        house = house.filter(
                     Q(city__icontains=query) |
                     Q(house_owner__icontains = query) |
                     Q(house_number__icontains=query) |
                     Q(cost_per_day__icontains=query)
                            )

    # pagination
    paginator = Paginator(house, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        house = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        house = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        house = paginator.page(paginator.num_pages)
    context = {
        'house': house,
    }
    return render(request, 'house_list.html', context)

def house_detail(request, id=None):
    detail = get_object_or_404(House,id=id)
    context = {
        "detail": detail
    }
    return render(request, 'house_detail.html', context)

def house_created(request):
    form = HouseForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/newhouse")
    context = {
        "form" : form,
        "title": "Create House"
    }
    return render(request, 'house_create.html', context)
# added
    return redirect('/newhouse')

def house_update(request, id=None):
    detail = get_object_or_404(House, id=id)
    form = HouseForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update House"
    }
    return render(request, 'house_create.html', context)

def house_delete(request,id=None):
    query = get_object_or_404(House,id = id)
    query.delete()

    house = House.objects.all()
    context = {
        'house': house,
    }
    return render(request, 'admin_index.html', context)

#order

def order_list(request):
    order = Order.objects.all()

    query = request.GET.get('q')
    if query:
        order = order.filter(
            Q(house_name__icontains=query)|
            Q(tenant_name__icontains=query)
        )

    # pagination
    paginator = Paginator(order, 4)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        order = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        order = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        order = paginator.page(paginator.num_pages)
    context = {
        'order': order,
    }
    return render(request, 'order_list.html', context)

def order_detail(request, id=None):
    detail = get_object_or_404(Order,id=id)
    context = {
        "detail": detail,
    }
    return render(request, 'order_detail.html', context)

def order_created(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
        # ✅ Redirect to payment page with order ID
        return redirect("payment_with_cart")  

    context = {
        "form": form,
        "title": "Create Order"
    }
    return render(request, 'order_create.html', context)

def order_update(request, id=None):
    detail = get_object_or_404(Order, id=id)
    form = OrderForm(request.POST or None, instance=detail)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
        "title": "Update Order"
    }
    return render(request, 'order_create.html', context)

def order_delete(request,id=None):
    query = get_object_or_404(Order,id = id)
    query.delete()
    return HttpResponseRedirect("/listOrder/")

def newhouse(request):
    new = House.objects.order_by('-id')
    #seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(city__icontains=query) |
            Q(house_owner__icontains=query) |
            Q(house_number__icontains=query) |
            Q(cost_per_day__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'house': new,
    }
   #addd
    messages.info(request, "Welcome" )
    return render(request, 'new_house.html', context)

def like_update(request, id=None):
    new = House.objects.order_by('-id')
    like_count = get_object_or_404(House, id=id)
    like_count.like+=1
    like_count.save()
    context = {
        'house': new,
    }
    return render(request,'new_house.html',context)

def popular_house(request):
    new = House.objects.order_by('-like')
    # seach
    query = request.GET.get('q')
    if query:
        new = new.filter(
            Q(city__icontains=query) |
            Q(house_owner__icontains=query) |
            Q(house_number__icontains=query) |
            Q(cost_per_day__icontains=query)
        )

    # pagination
    paginator = Paginator(new, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        new = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        new = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        new = paginator.page(paginator.num_pages)
    context = {
        'house': new,
    }
    return render(request, 'new_house.html', context)

def contact(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect("/house/newhouse/")
    context = {
        "form": form,
        "title": "Contact With Us",
    }
    return render(request,'contact.html', context)

#-----------------Admin Section-----------------

def admin_house_list(request):
    house = House.objects.order_by('-id')

    query = request.GET.get('q')
    if query:
        house = house.filter(
            Q(city__icontains=query) |
            Q(house_owner__icontains=query) |
            Q(house_number__icontains=query) |
            Q(cost_per_day__icontains=query)
        )

    # pagination
    paginator = Paginator(house, 12)  # Show 15 contacts per page
    page = request.GET.get('page')
    try:
        house = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        house = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        house = paginator.page(paginator.num_pages)
    context = {
        'house': house,
    }
    return render(request, 'admin_index.html', context)

def admin_msg(request):
    msg = PrivateMsg.objects.order_by('-id')
    context={
        "house": msg,
    }
    return render(request, 'admin_msg.html', context)

def msg_delete(request,id=None):
    query = get_object_or_404(PrivateMsg, id=id)
    query.delete()
    return HttpResponseRedirect("/message/")


    ##Added to yenepat ao==oatnebt 
def payment_with_cart(request):
    obj = {
        "process": "Cart",
        "successUrl": "http://localhost:8000/success",
        "ipnUrl": "http://localhost:8000/ipn",
        "cancelUrl": "http://localhost:8000/cancel",
        "merchantId": "SB1151",
        "merchantOrderId": "l710.0",
        "expiresAfter": 24,
        "totalItemsDeliveryFee": 19,
        "totalItemsDiscount": 1,
        "totalItemsHandlingFee": 12,
        "totalItemsTax1": 250,
        "totalItemsTax2": 0
    }
    cart = {
        "cartitems": [

        {

            "itemId":"sku-01",

            "itemName":"sample item",

            "unitPrice":2300,

            "quantity":1

        },

        {

            "itemId":"sku-02",

            "itemName":"sample item 2",

            "unitPrice":2300,

            "quantity":2

        }

        ]
    }
    return render(request, 'index_cart.html', {'obj': obj, 'cart': cart})

def payment_with_express(request):
    house = House.objects.all()
    obj = {
        "process": "Express",
        "successUrl": "http://localhost:8000/success",
        "ipnUrl": "http://localhost:8000/ipn",
        "cancelUrl": "http://localhost:8000/cancel",
        "merchantId": "SB1724",
        "merchantOrderId": "l710.0",
        "expiresAfter": 24,
        "itemId": 60,
        "itemName": "House Rent",
        "unitPrice": House.cost_per_day,
        "quantity": 1,
        "discount": 0.0,
        "handlingFee": 0.0,
        "deliveryFee": 0.0,
        "tax1": 0.0,
        "tax2": 0.0
    }
    return render(request, 'index_express.html', {'obj': obj})

def success(request):
    return render(request, 'success.html')
    

def cancel(request):
    return render(request, 'cancel.html')

def ipn(request):
    return render(request, 'ipn.html')

def noweasy(request):
    return HttpResponse("hello")









#added for customer Authentecation
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes


#Test for password rest
def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'your email' , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect ("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})