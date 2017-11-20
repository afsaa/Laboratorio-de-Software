
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from .forms import contactForm
from .forms import emailForm


def contacto(request):
	title='Contacto'
	form = contactForm(request.POST or None)
	context = {'title': title, 'form':form, }

	if form.is_valid():
		name = form.cleaned_data['nombre']
		comment = form.cleaned_data['comentario']
		print  form.cleaned_data['email']
		subject = 'Mensaje de SexShop.com'
		message = '%s %s' %(comment, name)
		emailFrom = form.cleaned_data['email']
		emailTo = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, emailFrom, [emailFrom, 'sexshoplab@gmail.com'], fail_silently=False)
		title="Gracias !"
		confirm_message ="El mensaje ha sido enviado, te lo responderemos en breve. gracias por tu paciencia."
		context = {'title': title, 'confirm_message':confirm_message, }

	template = 'contacto\contacto.html'
	return render(request,template,context)

def email(request):
	title= 'Email'
	form = emailForm(request.POST or None)
	context = {'title': title, 'form':form, }

	if form.is_valid():
		comment = form.cleaned_data['comentario']
		print  form.cleaned_data['email'].split(" ")

		subject = 'Mensaje de SexShop.com'
		message = '%s' %(comment)
		emailTo = form.cleaned_data['email'].split(" ")
		email=EmailMessage(subject=subject, body=message, bcc=emailTo)
		
		email.send()
		form = emailForm()
	template = 'contacto\email.html'
	return render(request,template,context)