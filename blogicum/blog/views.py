from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Post, Category


def index(request):
    template = 'blog/index.html'
    current_time = now()
    post_list = Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    current_time = now()
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            pub_date__lte=current_time,
            category__is_published=True
        ),
        pk=id  # Ищем публикацию по первичному ключу (pk)
    )
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    current_time = now()
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    ).order_by('-pub_date')
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
