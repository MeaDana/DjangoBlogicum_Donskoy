from django.utils import timezone
from django.http import Http404
from django.shortcuts import render
from .models import Post, Category
from django.shortcuts import get_object_or_404


def index(request):
    current_time = timezone.now()
    post_list = Post.objects.filter(is_published=True,
                                    category__is_published=True,
                                    pub_date__lte=current_time
                                    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, id):
    current_time = timezone.now()
    post = get_object_or_404(Post, pk=id)

    if (post.pub_date > current_time
            or not post.is_published
            or not post.category.is_published):
        raise Http404("Page not found")
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category,
                                 slug=category_slug, is_published=True)
    current_time = timezone.now()

    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=current_time
    )
    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': post_list})
