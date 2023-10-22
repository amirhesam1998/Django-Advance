from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
# Create your models here.

class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length= 250 , unique= True)  
    is_staff = models.BooleanField(default= False)   #A boolean field that indicates whether the user can enter the admin site or not.
    is_active = models.BooleanField(default= True)   #A Boolean field indicating whether the user account is active or inactive.
    is_verified = models.BooleanField(default= False)   #A Boolean field indicating whether the user account is verified.
    first_name = models.CharField(max_length=20)

    USERNAME_FIELD = "email"    #This means that during user authentication, Django uses the email field for the username. In other words, users can log in with their email address instead of using a username
    REQUIRED_FIELDS = []   #Users must fill in these fields to register.

    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email
