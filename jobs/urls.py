from django.urls import path
from .views import (
    ApplyJobView,
    MyApplicationsView,
    JobApplicationsView,
    UpdateApplicationStatusView
)

urlpatterns = [

    path("jobs/<int:job_id>/apply/", ApplyJobView.as_view()),

    path("my-applications/", MyApplicationsView.as_view()),

    path("jobs/<int:job_id>/applications/", JobApplicationsView.as_view()),

    path("applications/<int:application_id>/status/",
         UpdateApplicationStatusView.as_view()),

]