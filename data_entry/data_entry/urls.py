from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

from front_end import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),
    path('', include('django.contrib.auth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('my_account/', views.my_account, name='my_account'),  
    path('manage_employees/', views.manage_employees, name='manage_employees'),
    path('edit-employee/<int:UserID>/', views.edit_employee, name='edit_employee'),
    path('update-employee/<int:UserID>/', views.update_employee, name='update_employee'),
    path('delete-employee/<int:UserID>/', views.delete_employee, name='delete_employee'),
    path('new_employee/', views.NewEmployee.as_view(), name='new_employee'),
    path('manage_contracts/', views.manage_contracts, name='manage_contracts'),  
    path('manage_contract/', views.manage_contract, name='manage_contract'), 
    path('manage_documents/', views.manage_documents, name='manage_documents'),  
    path('manage_documents_packs/', views.manage_documents_packs, name='manage_documents_packs'),  
    path('manage_categories/', views.manage_categories, name='manage_categories'),
    path('manage_jobs/', views.manage_jobs, name='manage_jobs'),    
    path('manage_roles/', views.manage_roles, name='manage_roles'),  
    path('manage_role/', views.manage_role, name='manage_role'),  
    path('password_reset/', lambda request: redirect('reset_password')),
    path('new_job/', views.new_job.as_view(), name='new_job'),
    path('edit-job/<int:JobID>/', views.edit_job, name='edit_job'),
    path('update-job/<int:JobID>/', views.update_job, name='update_job'),
    path('delete-job/<int:JobID>/', views.delete_job, name='delete_job'),
    path('new_document/', views.new_document.as_view(), name='new_document'),
    path('edit-document/<int:DocumentID>/', views.edit_document, name='edit_document'),
    path('update-document/<int:DocumentID>/', views.update_document, name='update_document'),
    path('delete-document/<int:DocumentID>/', views.delete_document, name='delete_document'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
