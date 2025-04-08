from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Contact, CommunicationLog

@login_required(login_url="/auth/login")
def contact_list(request):
    
    contacts = Contact.objects.all()
    return render(request, 'pages/contact/contact_list.html', {'contacts': contacts})