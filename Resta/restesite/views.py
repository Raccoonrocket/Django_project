from django.shortcuts import render

from restesite.forms import ContactForm
from restesite.models import MenuItem


def index(request):
    menu_brk = MenuItem.objects.filter(type__exact='BRK').order_by('?')[:6]
    menu_lun = MenuItem.objects.filter(type__exact='LUN').order_by('?')[:6]
    menu_din = MenuItem.objects.filter(type__exact='DIN').order_by('?')[:6]
    context = {'menu_brk': menu_brk, 'menu_lun': menu_lun, 'menu_din': menu_din}
    return render(
        request,
        'index.html',
        context=context
    )


def about(request):
    return render(
        request,
        'about.html'
    )


def contacts(request):
    context = {}
    if request.method == 'POST':
        pass
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'contacts.html',
        context=context,
    )
