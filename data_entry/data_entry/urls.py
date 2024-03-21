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
    path('manage_employee/', views.manage_employee, name='manage_employee'), 
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
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
