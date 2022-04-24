from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from about.forms import CreateAboutForm, UpdateAboutForm, DeleteAboutFrom
from about.models import AboutModel


class AboutView(ListView):
    model = AboutModel
    template_name = "about.html"


def create_about_view(request):

    context = {}

    form = CreateAboutForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreateAboutForm()

    context['form'] = form

    return render(request, 'page/create.html', context)


def update_about_view(request, id):
    context = {}

    article = get_object_or_404(AboutModel, id=id)

    if request.POST:
        form = UpdateAboutForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            # obj.save()
            context['success_message'] = "Updated"

    form = UpdateAboutForm(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/update.html', context)


def delete_about_view(request, id):

    context = {}

    article = get_object_or_404(AboutModel, id=id)

    if request.POST:
        form = DeleteAboutFrom(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            article = obj

    form = DeleteAboutFrom(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/delete.html', context)
