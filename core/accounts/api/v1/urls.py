from django.urls import path
from . import views
#from rest_framework.authtoken.views import ObtainAuthToken
app_name = "api-v1"

urlpatterns = [
    #registrations
    path("registration/",views.RegistrationApiView.as_view(),name = "registration"),
    #path('token/login/', ObtainAuthToken.as_view() , name='token-login'),
    path('token/login/' , views.CustomObtainAuthToken.as_view() , name = 'token-login'),
    path('token/logout/' , views.CustomDiscardAuthToken.as_view() , name = 'token-logout'),
    #set password
    #reset password
    #login token
    #login jwt


]

