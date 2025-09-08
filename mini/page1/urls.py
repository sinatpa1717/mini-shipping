from django.urls import path
from .views import home_page_web
from .views import login_page_web
from .views import signup_page_web
from .views import logout_page_web
from .views import upload_iteam_page
from .views import poshtibani_page_web

urlpatterns = [
    path("", login_page_web, name="login_page_web"),
    path("home/", home_page_web, name="home_page_web"),
    path("signup/", signup_page_web, name="signup_page_web"),
    path("logout/", logout_page_web, name="logout_page_web"),
    path("upload_iteam_page/", upload_iteam_page, name="upload_iteam_page"),
    path("poshtibani_page_web/", poshtibani_page_web, name="poshtibani_page_web"),
]
