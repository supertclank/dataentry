from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

class User(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    JobID = models.ForeignKey('Job', on_delete=models.CASCADE, null=True)
    RoleID = models.ForeignKey('Role', on_delete=models.CASCADE, null=True)
    
    Type_E = models.IntegerField(default=0)
    Address_One = models.CharField(max_length=255)
    Address_Two = models.CharField(max_length=255, blank=True, null=True)
    City = models.CharField(max_length=255)
    County = models.CharField(max_length=255)
    Postcode = models.CharField(max_length=10)
    Contact_Number = models.CharField(max_length=15)
    
    birthdate = models.DateField(default=date.today)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True)
    last_login = models.DateTimeField(default=date.today)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=date.today)

    def __str__(self):
        return self.username

class PasswordHistory(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Password = models.CharField(max_length=255, null=True)
    
    class Meta:
        verbose_name_plural = 'Password Histories'

class Job(models.Model):
    JobID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)
    Job_Name = models.CharField(max_length=255)
    Job_Description = models.TextField()
    
    def __str__(self):
        return f"{self.JobID} | {self.Job_Name} - {self.Job_Description}"

class Role(models.Model):
    RoleID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Security_Permissions = models.BooleanField(default=False)
    Document_Permissions = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.RoleID} | {self.Name} - {self.Description}"

class JobRole(models.Model):
    JobID = models.ForeignKey(Job, on_delete=models.CASCADE)
    RoleID = models.ForeignKey(Role, on_delete=models.CASCADE)
    CreatedBy_UserID = models.IntegerField(default=0)
    Created_Date = models.IntegerField(default=0)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Updated_Date = models.DateField(default=date.today)
    
class Contract(models.Model):
    ContractID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)
    Type_E = models.IntegerField(default=0)
    Guid = models.BinaryField()

class DocumentPack(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)
    Type_E = models.IntegerField(default=0)
    Name = models.TextField()

class DocumentPackItem(models.Model):
    Document_ID = models.IntegerField(default=0)
    DocumentPack_ID = models.IntegerField(default=0)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)

class Document(models.Model):
    DocumentID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    path = models.CharField(max_length=4096)
    Type_E = models.IntegerField(default=0)

class DocumentCategory(models.Model):
    DocumentID = models.ForeignKey(Document, on_delete=models.CASCADE)
    Category_ID = models.IntegerField(default=0)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)
    
    class Meta:
        verbose_name_plural = 'Document Categories'

class Category(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Created_Date = models.DateField(default=date.today)
    Updated_Date = models.DateField(default=date.today)
    Name= models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'Categories'