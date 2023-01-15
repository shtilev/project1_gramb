from django.shortcuts import render
from .models import feedback
from .forms import feedbackForm
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def answer(request):
    error = ''
    if request.method == 'POST':
        form = feedbackForm(request.POST)
        if form.is_valid():
            form.save()
            #send_mail('Заявка', form, 'Grambit', ['grambitpro@gmail.com'], fail_silently=False)
            return render(request, 'main/success.html')
        else:
            error = 'Форма была не верной'
    form = feedbackForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'feedback/feedback.html', data)