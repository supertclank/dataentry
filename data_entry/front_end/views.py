from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.template import loader
from models.models import Job, Document, User
from django.views.generic.edit import CreateView

def index(request):
    return redirect('registration\login.html')

def dashboard(request):
    user_count = User.objects.count()
    document_count = Document.objects.count()
    job_count = Job.objects.count()

    context = {'user_count': user_count, 'document_count': document_count, 'job_count': job_count}
    return render(request, 'dashboard.html', context)

def my_account(request):
    return render(request, 'my_account.html')

def manage_users(request):
    user_list = User.objects.all()

    if request.method == 'GET':
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')

        if first_name:
            user_list = user_list.filter(First_Name__icontains=first_name)
        if last_name:
            user_list = user_list.filter(Last_Name__icontains=last_name)
        if email:
            user_list = user_list.filter(Email_address__icontains=email)
            
    context = {'user_list': user_list}
    return render(request, 'manage_employees.html', context)

def edit_user(request, UserID):
    user = get_object_or_404(User, UserID=UserID)
    return render(request, 'edit_employee.html', {'user': user})

def update_user(request, UserID):
    if request.method == 'POST':
        user = User.objects.get(UserID=UserID)
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.birthdate = request.POST['birthdate']
        user.Address_One = request.POST['address_one']
        user.Address_Two = request.POST['address_two']
        user.City = request.POST['city']
        user.County = request.POST['county']
        user.Postcode = request.POST['postcode']
        user.email = request.POST['email']
        user.Contact_Number = request.POST['contact_number']
        user.password = request.POST['password']
        user.save()
        return redirect('manage_users')


def delete_user(request, UserID):
    user = get_object_or_404(User, UserID=UserID)
    if request.method == 'POST':
        user.delete()
        return redirect('manage_users')

class NewUser(CreateView):
    model = User
    template_name = 'new_employee.html'
    fields = ['username', 'first_name', 'last_name', 'birthdate', 'Address_One', 'Address_Two', 'City', 'County', 'Postcode', 'email', 'Contact_Number']
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('manage_users')


def manage_contracts(request):
    return HttpResponse()

def manage_contract(request):
    return HttpResponse()

def manage_documents(request):
    document_list = Document.objects.all()

    if request.method == 'GET':
        name = request.GET.get('name')
        description = request.GET.get('description')
        date = request.GET.get('date')

        if name:
            document_list = document_list.filter(Name__icontains=name)
        if description:
            document_list = document_list.filter(Description__icontains=description)
        if date:
            document_list = document_list.filter(Created_Date=date)

    context = {'document_list': document_list}
    template = loader.get_template('manage_documents.html')
    return HttpResponse(template.render(context, request))

def edit_document(request, DocumentID):
    document = get_object_or_404(Document, DocumentID=DocumentID)
    return render(request, 'edit_documents.html', {'document': document})

def update_document(request, DocumentID):
    if request.method == 'POST':
        document = Document.objects.get(DocumentID=DocumentID)
        document.Name = request.POST['name']
        document.Description = request.POST['description']
        document.save()
        return redirect('manage_documents')

def delete_document(request, DocumentID):
    if request.method == 'POST':
        document = get_object_or_404(Document, DocumentID=DocumentID)
        document.delete()
        return redirect('manage_documents')

class new_document(CreateView):
    model = Document
    fields = ['Name', 'Description', 'path', 'Type_E']
    template_name = 'new_document.html'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('manage_documents')

def manage_documents_packs(request):
    return HttpResponse()

def manage_categories(request):
    return HttpResponse()

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

def delete_job(request, JobID):
    if request.method == 'POST':
        job = get_object_or_404(Job, JobID=JobID)
        job.delete()
        return redirect('manage_jobs')

class new_job(CreateView):
    model = Job
    fields = ['Job_Name', 'Job_Description', 'Created_Date']
    template_name = 'new_job.html'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('manage_jobs')

def manage_roles(request):
    return HttpResponse()

def manage_role(request):
    return HttpResponse()

def password_reset_form(request):
    template = loader.get_template('password_reset_form.html')
    context = {}
    return HttpResponse(template.render(context, request))

def password_reset_done(request):
    template = loader.get_template('password_reset_done.html')
    context = {}
    return HttpResponse(template.render(context, request))

def password_reset_confirm(request):
    template = loader.get_template('password_reset_confirm.html')
    context = {}
    return HttpResponse(template.render(context, request))