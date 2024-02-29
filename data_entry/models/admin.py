from django.contrib import admin

from django.contrib import admin
from .models import User, PasswordHistory, Job, JobRole, Role, Contract, DocumentPack, DocumentCategory, DocumentPackItem, Document, Category

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(PasswordHistory)
class PasswordHistoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(JobRole)
class JobRoleAdmin(admin.ModelAdmin):
    pass

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass

@admin.register(DocumentPack)
class DocumentPackAdmin(admin.ModelAdmin):
    pass

@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(DocumentPackItem)
class DocumentPackItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
