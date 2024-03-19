from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404


def index(request):
    contacts = Contact.objects.filter(show=True)
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos -',
    }
    return render(
        request,
        'contact/index.html',
        context
        )


def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk= contact_id, show=True)
    site_title = f'{single_contact.first_name} {single_contact.last_name} -'

    context = {
        'contact': single_contact,
        'site_title': site_title
    }
    return render(
        request,
        'contact/contact.html',
        context
        )
def search(request):
    search_result = request.GET.get('q', '').strip()
    
    if search_result == '':
        return redirect('contact:index')
    
    contacts = Contact.objects.filter(show=True)\
    .filter(
            Q(first_name__icontains=search_result)|
            Q(phone__icontains=search_result) |
            Q(email__icontains=search_result) 
            )
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': search_result +' - ',
        'search_value' : search_result
    }
    return render(
        request,
        'contact/index.html',
        context
        )
