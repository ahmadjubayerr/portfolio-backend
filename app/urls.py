from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.my_profile, name="my-profile"),
    path("projects/", views.project_list, name="project-list"),
    path("favorite-projects/", views.favorite_project_list, name="favorite-project-list"),
    path("projects/<int:pk>/detail/", views.project_detail, name="project-detail"),
    path("contact/", views.contact,name="contact"),

    path("certifications/", views.my_certifications, name="certifications"),
    path("experience/", views.my_experience, name="experience"),
    path("educations/", views.my_educations, name="educations"),
]
