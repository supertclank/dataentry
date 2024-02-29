from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request)) 

def dashboard (request):
    template = loader.get_template('dashboard.html')
    context = {}
    return HttpResponse(template.render(context, request))  

def my_account (request):
    template = loader.get_template('my_account.html')
    context = {}
    return HttpResponse(template.render(context, request)
    )
    
def manage_employees (request):
    template = loader.get_template('manage_employees.html')
    context = {}
    return HttpResponse(template.render(context, request)
    )
    
def manage_employee (request):
    return HttpResponse(
        
    )
    
def manage_contracts (request):
    return HttpResponse(
        
    )
    
def manage_contract (request):
    return HttpResponse(
        
    )

def manage_documents (request):
    template = loader.get_template('manage_documents.html')
    context = {}
    return HttpResponse(template.render(context, request)
    )
    
def manage_documents_packs (request):
    return HttpResponse(
        
    )
    
def manage_categories (request):
    return HttpResponse(
        
    )
    
def manage_jobs (request):
    template = loader.get_template('manage_jobs.html')
    context = {}
    return HttpResponse(template.render(context, request)
    )
    
def manage_job (request):
    return HttpResponse(
        
    )
    
def manage_roles (request):
    return HttpResponse(
        
    )
    
def manage_role (request):
    return HttpResponse(
        
    )

