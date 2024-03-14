from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from models.models import Job
from django.views.generic.edit import CreateView
from data_entry.form import JobForm

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
    
def manage_jobs(request):
    job_list = Job.objects.all()

    if request.method == 'GET':
        job_name = request.GET.get('job_name')
        job_description = request.GET.get('job_description')
        date = request.GET.get('date')

        if job_name:
            job_list = job_list.filter(Job_Name__icontains=job_name)
        if job_description:
            job_list = job_list.filter(Job_Description__icontains=job_description)
        if date:
            job_list = job_list.filter(Created_Date=date)

    context = {'job_list': job_list}
    
    template = loader.get_template('manage_jobs.html')
    return HttpResponse(template.render(context, request))
       
def edit_job(request, JobID):
    job = get_object_or_404(Job, JobID=JobID)
    return render(request, 'edit_job.html', {'job': job})

def update_job(request, JobID):
    if request.method == 'POST':
        job = Job.objects.get(JobID=JobID)
        job.Job_Name = request.POST['job_name']
        job.Job_Description = request.POST['job_description']
        job.save()
        return redirect('manage_jobs')
    
class new_job(CreateView):
    model = Job
    fields = ['Job_Name', 'Job_Description', 'Created_Date']
    template_name = 'new_job.html'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('manage_jobs')
    
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