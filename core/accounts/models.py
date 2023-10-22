from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
from django.utils.translation import gettext_lazy as _            #"Using ugettext_lazy means that you don't translate texts to a specific language (for example, English to French or Farsi). Instead, you say "these texts are translatable" and Django uses its own language translation process at runtime. This feature allows you to easily translate your apps for different languages and present them to people who use different languages."
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self , email , password , **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_('the email must be set'))
        email = self.normalize_email(email)   #check validation email by normalize_email method in BaseUserManager
        user = self.model(email = email , **extra_fields)  #create user model by valid email (check in line up) and extra fields
        user.set_password(password)    #ser password for user by set_password method in BaseUserManager
        user.save()
        return user
    def create_superuser(self , email , password , **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff' , True)
        extra_fields.setdefault('is_superuser' , True)
        extra_fields.setdefault('is_active' , True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser , PermissionsMixin):
    """
    Custom user model for our app
    """

    
    email = models.EmailField(max_length= 250 , unique= True)  
    is_staff = models.BooleanField(default= False)   #A boolean field that indicates whether the user can enter the admin site or not.
    is_active = models.BooleanField(default= True)   #A Boolean field indicating whether the user account is active or inactive.
    is_verified = models.BooleanField(default= False)   #A Boolean field indicating whether the user account is verified
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)

    USERNAME_FIELD = "email"    #This means that during user authentication, Django uses the email field for the username. In other words, users can log in with their email address instead of using a username
    REQUIRED_FIELDS = []   #Users must fill in these fields to register.
    objects = UserManager()

    created_date = models.DateTimeField(auto_now_add= True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE) 
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True , null= True)
    description = models.TextField()

    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

@receiver(post_save , sender = User)    #SIGNALS : When the 'user' model is made, add it to 'Profile' model as well
def save_profile(sender , instance , created , **kwargs):
    if created:  #If it is made, make it, if it is not made, edit it and don't make anything
        Profile.objects.create(user = instance)