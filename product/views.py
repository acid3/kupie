from re import template
from django.shortcuts import render, get_object_or_404, redirect
# from matplotlib.style import context
from product.models import CategoryClass, ProductBase, ProductImages
from django.db.models import Count
from .addForm import addProductForm
from .contactForm import msgForm
from privmsg.models import prvMsg


# Create your views here.


def productlist(request, category_slug=None):
    category = None
    # productlist = ProductBase.objects.all()
    productlist = ProductBase.objects.order_by("-publication_time")
    categorylist = CategoryClass.objects.annotate(
        total_products=Count('productbase'))
    count = ProductBase.objects.all().count

    if category_slug:
        category = get_object_or_404(
            CategoryClass, category_slug=category_slug)
        productlist = productlist.filter(category=category)
    # kat_count = CategoryClass.objects.filter

    template = 'Product/product_list.html'
    context = {'product_list': productlist,
               'category_list': categorylist,
               'category': category,
               'count': count,
               }

    return render(request, template, context)


def productdetail(request, product_slug):
    productdetail = ProductBase.objects.get(slug=product_slug)
    productimages = ProductImages.objects.filter(product=productdetail)

    template = 'Product/product_detail.html'
    context = {'product_detail': productdetail,
               'product_images': productimages,
               }

    return render(request, template, context)


def productcontact(request, product_slug):
    template = 'Product/detail_contact.html'
    details = ProductBase.objects.get(slug=product_slug)

    if request.method == 'POST':
        user_form = msgForm(data=request.POST)

        user_form.instance.sender_id = request.user
        user_form.instance.reciver_id = details.author
        user_form.instance.title = details.title
        user_form.instance.is_open = False

        if user_form.is_valid():
            user_form.save()
            return redirect('/products')

    else:
        user_form = msgForm()

    context = {'user_form': user_form,
               'detale': details,
               }

    return render(request, template, context)


def addProduct(request):
    if request.method == 'POST':
        user_form = addProductForm(data=request.POST)
        if user_form.is_valid():
            # pobiera i automatycznie wpisuje do modelu user_id
            user_form.instance.author = request.user
            user_form.save()
            return redirect('/products')

    else:
        user_form = addProductForm()

    context = {'user_form': user_form}

    return render(request, 'Product/dodaj.html', context)
