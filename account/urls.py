from django.urls import path
from .views import home, login_page, logout_page, SignUpView

urlpatterns = [
    path('', home,name="home"),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('signup/', SignUpView.as_view(), name='signup'),
]