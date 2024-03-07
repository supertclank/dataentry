from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from models.models import Job

def index(request):
    
    return redirect('registration\login.html')

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
    Job_list = Job.objects.all()
    template = loader.get_template('manage_jobs.html')
    context = {'Job_list': Job_list}
    return HttpResponse(template.render(context, request))
    
    
def manage_job (request):
    template = loader.get_template('manage_job.html')
    context = {}
    return HttpResponse(template.render(context, request)
    )
    
def manage_roles (request):
    return HttpResponse(
        
    )
    
def manage_role (request):
    return HttpResponse(
        
    )
def password_reset_form (request):
    template = loader.get_template('password_reset_form.html')
    context = {}
    return HttpResponse(template.render(context, request))

def password_reset_done (request):
    template = loader.get_template('password_reset_done.html')
    context = {}
    return HttpResponse(template.render(context, request))

def password_reset_confirm (request):
    template = loader.get_template('password_reset_confirm.html')
    context = {}
    return HttpResponse(template.render(context, request))