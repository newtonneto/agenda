from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .contact import Contact

# Create your views here.
def index(request):
    if not request.session['contact_list']:
        request.session['contact_list'] = []
    """ else:
        request.session['contact_list'] = [] """

    context = {
        'contact_list': request.session['contact_list'],
    }

    return render(request, 'contatos/index.html', context)

def new_contact(request):
    return render(request, 'contatos/novo.html')

def edit_contact(request):
    return render(request, 'contatos/index.html')

def save_contact(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    #contact = Contact(name, phone, email)
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
    }

    #print(contact)
    contact_list = request.session['contact_list']
    contact_list.append(contact)
    request.session['contact_list'] = contact_list

    print(request.session['contact_list'])

    return render(request, 'contatos/novo.html')

def remove_contact(request):
    return render(request, 'contatos/index.html')