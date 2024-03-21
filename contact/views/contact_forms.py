from django.shortcuts import render
from contact.forms import ContactForm

def create(request):
    post = request.POST.get('first_name').strip(); print(post)
    
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context
        )

    
    context = {
        'form': ContactForm()
    }
    return render(
        request,
        'contact/create.html',
        context
        )
