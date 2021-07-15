from django.db.models import Q
from django.shortcuts import render
from .models import Photos, Category


# Create your views here.


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def index(request):
    photos = Photos.objects.all().order_by('-date')
    context = {'photos': photos}
    return render(request, 'photos/index.html', context)


def category_list(request, slug=None):
    category = Category.objects.get(slug__iexact=slug)
    photos = Photos.objects.filter(category=category)
    context = {'category': category, 'photos': photos}
    return render(request, 'photos/category.html', context)


def search_result(request):
    query = request.GET.get('search')
    search_obj = Photos.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )
    context = {'search_obj': search_obj, 'query': query}
    return render(request, 'photos/search.html', context)


def post_detail(request, pk):
    salom = Photos.objects.get(id=pk)
    context = {'photo': salom}
    return render(request, 'photos/detail.html', context)
