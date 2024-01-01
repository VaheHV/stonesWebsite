from django.shortcuts import render
from .models import Blog, Product


def home(request):
    blogs = Blog.objects.all()[:4]
    return render(request, 'store/home.html', {'blogs': blogs})


def blog(request):
    tag = request.GET.get('tag')

    if tag:
        blogs = Blog.objects.filter(tag=tag)
    else:
        blogs = Blog.objects.all()

    tags = Blog.objects.values('tag').distinct()

    return render(request, 'store/blog.html', {'blogs': blogs, 'tags': tags})


def about(request):
    return render(request, 'store/about.html')


def article_page(request, pk):
    article = Blog.objects.get(id=pk)
    return render(request, 'store/article.html', {'article': article})


def product_page(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product_page.html', {'product': product})


def products(request):
    category = request.GET.get('category')
    tag = request.GET.get('tag')

    if category and tag:
        products = Product.objects.filter(category=category, tag=tag)
    elif category:
        products = Product.objects.filter(category=category)
    elif tag:
        products = Product.objects.filter(tag=tag)
    else:
        products = Product.objects.all()

    categories = Product.CATEGORY_CHOICES
    tags = Product.objects.values('tag').distinct()

    return render(request, 'store/products.html', {'products': products, 'categories': categories, 'tags': tags})
