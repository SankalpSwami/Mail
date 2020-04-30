from django.shortcuts import render
from .models import Compose
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView
from django.core.mail import send_mail
from django.conf import settings

def inbox(request):
	context = {
		'composes': Compose.objects.filter(to=request.user.email)
	}
	return render(request, 'blog/inbox.html', context)

def sent(request):
	context = {
		'composes': Compose.objects.filter(author=request.user)
	}
	return render(request, 'blog/sent.html', context)

class ComposeDetailView(DetailView):
	model = Compose		

class ComposeCreateView(LoginRequiredMixin, CreateView):
    model = Compose
    fields = ['to', 'subject','body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def mail(request):

	if request.method == 'POST':
		message = request.POST['message']
		to = request.POST['to']
		subject = request.POST['subject']

		send_mail(subject,
		 message, 
		 settings.EMAIL_HOST_USER,
		 [to], fail_silently=False) 
	return render(request, 'blog/mail.html')	

