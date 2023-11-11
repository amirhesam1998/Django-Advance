from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# getting user model objects in everywhere by AUTH_USER_MODEL in settings.py
# User = get_user_model()


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        "accounts.Profile", on_delete=models.CASCADE
    )  # When a user (or the related record in the User model) is deleted, all the posts that are related to this user (posts that have this user as the author) are also deleted.
    image = models.ImageField(
        null=True, blank=True
    )  # That is, it is not mandatory. null for databases , blank for input in tamplates
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )  # This means that if a record is deleted in the Category model, every post associated with this category will receive a null value and will not be associated with the deleted category. This approach is useful when you need records in the related model to remain valid even if the related record in the original model is deleted.
    created_date = models.DateTimeField(
        auto_now_add=True
    )  # The value of this field is set to the current exact date and time of the database (server time) and the user cannot fill this field manually.
    updated_date = models.DateTimeField(
        auto_now=True
    )  # The value of this field is set to the current exact date and time of the database (server time). This is done automatically and the user does not need to manually intervene in this field.
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
