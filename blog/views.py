from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from blog.forms import CreateBlogForm, UpdateBlogForm, DeleteBlogFrom
from blog.models import BlogModel


class BlogView(ListView):
    model = BlogModel
    template_name = "blog.html"


def create_blog_view(request):

    context = {}

    form = CreateBlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreateBlogForm()

    context['form'] = form

    return render(request, 'page/create.html', context)


def update_blog_view(request, id):
    context = {}

    article = get_object_or_404(BlogModel, id=id)

    if request.POST:
        form = UpdateBlogForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            # obj.save()
            context['success_message'] = "Updated"

    form = UpdateBlogForm(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/update.html', context)


def delete_blog_view(request, id):

    context = {}

    article = get_object_or_404(BlogModel, id=id)

    if request.POST:
        form = DeleteBlogFrom(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            article = obj

    form = DeleteBlogFrom(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/delete.html', context)
