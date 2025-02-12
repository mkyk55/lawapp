from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home_page(request):
    print("home page")
    context = {}
    return render(request, 'home/home.html', context)

def about_page(request):
    print("about page")
    context = {}
    return render(request, 'about/about.html', context)


def contact_us(request):
    context = {}
    if request.method == "POST":
        print("post form") 
        name = request.POST.get("name")   
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        print(name)
        print(email)
        print(subject)
        print(message)
        if name and email and subject and message:
            try:
                send_mail(subject,email + " :: has sent you messgae from Advocate Associates: " + message, settings.EMAIL_HOST_USER, ['advocate.mayank555@gmail.com'])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'

   
    return render(request, 'contact/contact.html', context)


def criminal_cases(request):
    context = {}
    return render(request, 'criminal/criminal.html', context)

def civil_cases(request):
    context = {}
    return render(request, 'civil/civil.html', context)

def matrimonial_cases(request):
    context = {}
    return render(request, 'matrimonial/matrimonial.html', context)

def family_cases(request):
    context = {}
    return render(request, 'family/family.html', context)

def cyber_cases(request):
    context = {}
    return render(request, 'cyber/cyber.html', context)

def mediation_cases(request):
    context = {}
    return render(request, 'mediation/mediation.html', context)

def negotiable_cases(request):
    context = {}
    return render(request, 'negotiable/negotiable.html', context)

def labour_cases(request):
    context = {}
    return render(request, 'labour/labour.html', context)

def team(request):
    context = {}
    return render(request, 'team/team.html', context)