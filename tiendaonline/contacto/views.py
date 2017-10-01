
from django.shortcuts import render

from .forms import contactForm
# Create your views here.
def contacto(request):
	form = contactForm(request.POST or None)

	if form.is_valid():
		print form.cleaned_data['email']
	context = locals()
	template = 'contacto.html'
	return render(request,template,context)