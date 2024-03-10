from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .models import Post, Comment, Project
from django.http import Http404
from .forms import CommentForm, ContactForm

def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    return render(request, 'blogapp/post_list.html', {'posts': posts})

# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404('No Post Found')
#     # post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
#
#     return render(request, 'blogapp/post_detail.html', {'post': post})

# def post_detail(request, slug):
#     try:
#         post = Post.published.get(slug=slug)
#     except Post.DoesNotExist:
#         raise Http404('No Post Found')
#     # post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
#
#     return render(request, 'blogapp/post_detail.html', {'post': post})

def home(request):
   return render(request, 'blogapp/home.html')

# @require_POST
# def post_comment(request, slug):
#     # post = get_object_or_404(Post, slug=slug, status='published')
#     post = Post.published.get(slug=slug)
#     comment = None
#     form = CommentForm(data=request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         comment.post = post
#         comment.save()
#     return render(request, 'blogapp/post_detail.html', {
#         'post': post, 'form': form, 'comment': comment
#     })

def post_detail(request, slug):
    try:
        post = Post.published.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404('No Post Found')

    active_comments = post.comments.filter(active=True)
    active_comments_count = post.comments.filter(active=True).count()

    comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # Clear the form after successful submission
            form = CommentForm()
            return render(request, 'blogapp/success_sending_message.html')
    else:
        form = CommentForm()

    return render(request, 'blogapp/post_detail.html', {
        'post': post,
        'form': form,
        'comment': comment,
        'active_comments': active_comments,
        'active_comments_count': active_comments_count
    })

# def success_url(request):
#     return render(request, 'blogapp/success_sending_message.html')

# def contact_us(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return render(request, 'blogapp/success_sending_message.html')
#     else:
#         form = ContactForm()
#
#     return render(request, 'blogapp/contact_us.html', {'form': form})





def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add a success message here
            return render(request, 'blogapp/success_sending_message.html')  # Replace 'success_url' with the URL name of your success page
    else:
        form = ContactForm()

    return render(request, 'blogapp/contact_us.html', {'form': form})


def blog(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.get_page(page_number)
    return render(request, 'blogapp/blog.html', {'posts': posts, 'current_page': int(page_number)})

def project(requset):
    projects = Project.objects.all()
    return render(requset, 'blogapp/projects.html', {'projects': projects})