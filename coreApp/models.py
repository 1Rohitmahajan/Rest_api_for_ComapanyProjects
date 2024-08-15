from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name



#if not use django admin user name
# class User(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE)
#     email=models.CharField(max_lenght=100,blank=True)
#     phone_number = models.CharField(max_length=15, blank=True)
#     password = models.CharField(max_length=25, blank=True)
#     comform_password = models.CharField(max_length=25, blank=True)

#     def __str__(self):
#         return self.user.username