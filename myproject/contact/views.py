from django.shortcuts import render, redirect
from .models import ContactMessage

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect('contact_success')
    return render(request, 'contact/about.html')
