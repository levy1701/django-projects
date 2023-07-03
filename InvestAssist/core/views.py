from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.core.mail import send_mail


from item.models import Item 
from .forms import SignupForm

def index(request):
    items = Item.objects.all()

    return render(request, 'core/index.html', {
        'items': items,
    })

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Enviar o e-mail de confirmação
            send_mail(
                'Confirmação de Cadastro',
                f'Olá {user.username}, obrigado por se cadastrar em nossa aplicação InvestAssist.',
                'seuemail@example.com',  # Remetente do e-mail
                [user.email],  # Destinatário do e-mail
                fail_silently=False,
            )

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


def logout(request):
    auth_logout(request)
    return redirect('core:index')

