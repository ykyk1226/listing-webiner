from django.urls import path
from users.views.signupView import SignupView

app_name = 'users'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]