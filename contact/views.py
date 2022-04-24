from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from contact.forms import CreateContactForm, UpdateContactForm, DeleteContactFrom
from contact.models import ContactModel


class ContactView(ListView):
    model = ContactModel
    template_name = "contact.html"


def create_contact_view(request):

    context = {}

    form = CreateContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = CreateContactForm()

    context['form'] = form

    return render(request, 'page/create.html', context)


def update_contact_view(request, id):
    context = {}

    article = get_object_or_404(ContactModel, id=id)

    if request.POST:
        form = UpdateContactForm(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            form.save()
            # obj.save()
            context['success_message'] = "Updated"

    form = UpdateContactForm(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/update.html', context)


def delete_contact_view(request, id):

    context = {}

    article = get_object_or_404(ContactModel, id=id)

    if request.POST:
        form = DeleteContactFrom(request.POST or None, request.FILES or None, instance=article)
        if form.is_valid():
            obj = form.save(commit=True)
            obj.save()
            context['success_message'] = "Updated"
            article = obj

    form = DeleteContactFrom(
        initial={
            'title': article.title,
            'body': article.body,
            'primer': article.primer,
        }
    )

    context['form'] = form
    return render(request, 'page/delete.html', context)
