from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.template import loader
from models.models import Job, Document, User, Role
from django.contrib.auth.decorators import login_required

def index(request):
    return redirect('registration/login.html')

@login_required
def dashboard(request):
    user_count = User.objects.count()
    document_count = Document.objects.count()
    job_count = Job.objects.count()
    role_count = Role.objects.count()

    context = {
        'user_count': user_count,
        'document_count': document_count,
        'job_count': job_count,
        'role_count': role_count,
    }
    return render(request, 'dashboard.html', context)

@login_required
def my_account(request):
    user = request.user
    return render(request, 'my_account.html', {'user': user})

@login_required
def my_contract(request):
    user = request.user
    contract = user.user_contract
    return render(request, 'my_contract.html', {'user': user, 'contract': contract})

@login_required
def manage_users(request):
    user_list = User.objects.all()

    if request.method == 'GET':
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')

        if first_name:
            user_list = user_list.filter(first_name__icontains=first_name)
        if last_name:
            user_list = user_list.filter(last_name__icontains=last_name)
        if email:
            user_list = user_list.filter(email__icontains=email)
            
    context = {'user_list': user_list}
    return render(request, 'manage_employees.html', context)

@login_required
def edit_user(request, UserID):
    user = get_object_or_404(User, UserID=UserID)
    return render(request, 'edit_employee.html', {'user': user})

@login_required
def update_user(request, UserID):
    user = get_object_or_404(User, UserID=UserID)
    
    if request.method == 'POST':
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
        
        if 'password' in request.POST and request.POST['password']:
            user.set_password(request.POST['password'])


        if 'user_contract' in request.FILES:
            user.user_contract = request.FILES['user_contract']
        
        user.save()
        return redirect('manage_users')
    
    return render(request, 'edit_employee.html', {'user': user})

@login_required
def delete_user(request, UserID):
    user = get_object_or_404(User, UserID=UserID)
    if request.method == 'POST':
        user.delete()
        return redirect('manage_users')

class NewUser(CreateView):
    model = User
    template_name = 'new_employee.html'
    fields = ['username', 'first_name', 'last_name', 'birthdate', 'Address_One', 'Address_Two', 'City', 'County', 'Postcode', 'email', 'Contact_Number', 'profile_image']
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('manage_users')

@login_required
def manage_contracts(request):
    return HttpResponse()

@login_required
def manage_contract(request):
    return HttpResponse()

@login_required
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

@login_required
def view_document(request, DocumentID):
    document = get_object_or_404(Document, pk=DocumentID)
    return render(request, 'view_document.html', {'document': document})

@login_required
def edit_document(request, DocumentID):
    document = get_object_or_404(Document, DocumentID=DocumentID)
    return render(request, 'edit_documents.html', {'document': document})

@login_required
def update_document(request, DocumentID):
    document = get_object_or_404(Document, DocumentID=DocumentID)
    if request.method == 'POST':
        document.Name = request.POST['name']
        document.Description = request.POST['description']

        if 'document_file' in request.FILES:
            document.Document_file = request.FILES['document_file']
            
        document.save()
        
        return redirect('manage_documents')
    
    return render(request, 'edit_documents.html', {'document': document})

@login_required
def delete_document(request, DocumentID):
    if request.method == 'POST':
        document = get_object_or_404(Document, DocumentID=DocumentID)
        document.delete()
        return redirect('manage_documents')

class new_document(CreateView):
    model = Document
    fields = ['Name', 'Description', 'Document_file']
    template_name = 'new_document.html'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('manage_documents')

def manage_documents_packs(request):
    return HttpResponse()

def manage_categories(request):
    return HttpResponse()

@login_required
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

@login_required
def edit_job(request, JobID):
    job = get_object_or_404(Job, JobID=JobID)
    return render(request, 'edit_job.html', {'job': job})

@login_required
def update_job(request, JobID):
    if request.method == 'POST':
        job = Job.objects.get(JobID=JobID)
        job.Job_Name = request.POST['job_name']
        job.Job_Description = request.POST['job_description']
        job.save()
        return redirect('manage_jobs')

@login_required
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

@login_required
def manage_roles(request):
    role_list = Role.objects.all()

    Role_name = request.GET.get('Role_name')
    Role_description = request.GET.get('Role_description') 
    Security_Permissions = request.GET.get('Security_Permissions')
    Document_Permissions = request.GET.get('Document_Permissions')    

    if Role_name:
        role_list = role_list.filter(Name__icontains=Role_name)
        
    if Role_description:
        role_list = role_list.filter(Description__icontains=Role_description)
        
    if Security_Permissions is not None:
        Security_Permissions = Security_Permissions.lower() in ['true', '1', 'yes']
        role_list = role_list.filter(Security_Permissions=Security_Permissions)
        
    if Document_Permissions is not None:
        Document_Permissions = Document_Permissions.lower() in ['true', '1', 'yes']
        role_list = role_list.filter(Document_Permissions=Document_Permissions)

    context = {'role_list': role_list}
    template = loader.get_template('manage_roles.html')
    return HttpResponse(template.render(context, request))


@login_required
def edit_role(request, RoleID):
    role = get_object_or_404(Role, RoleID=RoleID)
    return render(request, 'edit_role.html', {'role': role})

@login_required
def update_role(request, RoleID):
    if request.method == 'POST':
        role = Role.objects.get(RoleID=RoleID)
        role.Name = request.POST['Name']
        role.Description = request.POST['Description']
        role.Security_Permissions = request.POST['Security_Permissions']
        role.Document_Permissions = request.POST['Document_Permissions']
        role.save()
        return redirect('manage_roles')

@login_required
def delete_role(request, RoleID):
    if request.method == 'POST':
        role = get_object_or_404(role, RoleID=RoleID)
        role.delete()
        return redirect('manage_roles')

class new_role(CreateView):
    model = Role
    fields = ['Name', 'Description', 'Security_Permissions', 'Document_Permissions']
    template_name = 'new_role.html'
    
    def form_valid(self, form):
        self.object = form.save()
        return redirect('manage_roles')

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
