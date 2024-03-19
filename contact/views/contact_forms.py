from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404



def create(request):
    post = request.POST
    context = {
    }
    return render(
        request,
        'contact/create.html',
        context
        )
