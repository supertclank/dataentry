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
    path('manage_users/', views.manage_users, name='manage_users'),
    path('edit_user/<int:UserID>/', views.edit_user, name='edit_user'), 
    path('update_user/<int:UserID>/', views.update_user, name='update_user'),
    path('delete_user/<int:UserID>/', views.delete_user, name='delete_user'),
    path('new_user/', views.NewUser.as_view(), name='new_user'),
    path('manage_contracts/', views.manage_contracts, name='manage_contracts'),  
    path('manage_contract/', views.manage_contract, name='manage_contract'), 
    path('manage_documents/', views.manage_documents, name='manage_documents'),  
    path('manage_documents_packs/', views.manage_documents_packs, name='manage_documents_packs'),  
    path('manage_categories/', views.manage_categories, name='manage_categories'),
    path('manage_jobs/', views.manage_jobs, name='manage_jobs'),    
    path('manage_roles/', views.manage_roles, name='manage_roles'),  
    path('edit_role/<int:RoleID>', views.edit_role, name='edit_role'),
    path('update_role/<int:RoleID>', views.update_role, name='update_role'),
    path('delete_role/<int:RoleID>', views.delete_role, name='delete_role'),
    path('new_role/', views.new_role.as_view(), name='new_role'), 
    path('password_reset/', lambda request: redirect('reset_password')),
    path('new_job/', views.new_job.as_view(), name='new_job'),
    path('edit_job/<int:JobID>/', views.edit_job, name='edit_job'),
    path('update_job/<int:JobID>/', views.update_job, name='update_job'),
    path('delete_job/<int:JobID>/', views.delete_job, name='delete_job'),
    path('new_document/', views.new_document.as_view(), name='new_document'),
    path('edit_document/<int:DocumentID>/', views.edit_document, name='edit_document'),
    path('update_document/<int:DocumentID>/', views.update_document, name='update_document'),
    path('delete_document/<int:DocumentID>/', views.delete_document, name='delete_document'),
    path('my_contract/', views.my_contract, name='my_contract'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
