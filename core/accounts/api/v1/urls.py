from django.urls import path
from . import views

app_name = "api-v1"

urlpatterns = [
    #registrations
    path("registration/",views.RegistrationApiView.as_view(),name = "registration")
    #set password
    #reset password
    #login token
    #login jwt


]

