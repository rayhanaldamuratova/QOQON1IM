from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from core.models import SchoolInfo


def contact(request):
    school = SchoolInfo.objects.first()
    if request.method == 'POST':
        ContactMessage.objects.create(
            full_name=request.POST.get('full_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            subject=request.POST.get('subject', ''),
            message=request.POST.get('message', ''),
        )
        messages.success(request, "Murojaatingiz qabul qilindi. Tez orada javob beramiz!")
        return redirect('contact:contact')
    return render(request, 'contact/contact.html', {'school': school})



