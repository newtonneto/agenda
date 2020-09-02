from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
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

def save_contact(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
    }

    #print(contact)
    contact_list = request.session['contact_list']
    contact_list.append(contact)
    request.session['contact_list'] = contact_list

    return render(request, 'contatos/novo.html')

def edit_contact(request, id):
    contact = request.session['contact_list'][id]

    context = {
        'id': id,
        'contact': contact,
    }

    return render(request, 'contatos/editar.html', context)

def save_edit_contact(request, id):
    contact = {
        'name': request.POST['name'],
        'phone': request.POST['phone'],
        'email': request.POST['email'],
    }

    request.session['contact_list'][id] = contact

    return redirect(reverse('contatos:index'))
    

def remove_contact(request, id):
    request.session['contact_list'].pop(id)

    return redirect(reverse('contatos:index'))