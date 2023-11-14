from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from .users import User






class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()

    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email


@receiver(
    post_save, sender=User
)  # SIGNALS : When the 'user' model is made, add it to 'Profile' model as well
def save_profile(sender, instance, created, **kwargs):
    if (
        created
    ):  # If it is made, make it, if it is not made, edit it and don't make anything
        Profile.objects.create(user=instance)
