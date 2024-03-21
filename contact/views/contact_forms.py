from django.shortcuts import redirect, render
from contact.forms import ContactForm

def create(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        context = {
            'form': form
        }
        if form.is_valid():
            print('form salvo')
            form.save()
            return redirect('contact:create')
        return render(
            request,
            'contact/create.html',
            context
        )

    
    context = {
        'form': form
    }
    return render(
        request,
        'contact/create.html',
        context
        )
