"""courseWork URL Configuration"""

from django.contrib import admin
from django.urls import include, path

from main import views

urlpatterns = [
    path("baton/", include("baton.urls")),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("numericmethods/", views.numericMehods, name="numeric"),
    path("numericmethods/matrixrules", views.matrixLawOfEquality, name="matrix-loe"),
    path("numericmethods/determinant", views.determinant, name="determinant"),
    path("login/", views.LoginView.as_view(), name="login_url"),
    path("logout/", views.logout_view, name="logout_url"),
    path("registration/", views.RegistrView.as_view(), name="reg_url"),
    path("profile/", views.profile, name="profile"),
    path("numericmethods/gauss", views.gauss_method, name="gauss"),
    path("quiz/<int:quiz_id>/", views.quiz, name="quiz"),
    path("quiz/<int:quiz_id>/submit/", views.submit_quiz, name="submit_quiz"),
    path("numericmethods/crammer", views.crammer_method, name="crammer"),
    path("numericmethods/iterative", views.iterative_method, name="iterative"),
]

handler404 = "main.views.page_not_found"
