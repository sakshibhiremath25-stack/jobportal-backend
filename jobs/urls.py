from django.urls import path
from .views import (
    JobListView,
    ApplyJobView,
    MyApplicationsView,
    JobApplicationsView,
    UpdateApplicationStatusView,
)

urlpatterns = [
    # List all jobs / Create job
    path('jobs/', JobListView.as_view(), name='job-list'),

    # Apply for a job
    path('jobs/<int:job_id>/apply/', ApplyJobView.as_view(), name='apply-job'),

    # Candidate → view their applications
    path('my-applications/', MyApplicationsView.as_view(), name='my-applications'),

    # Employer → view applications for a job
    path('jobs/<int:job_id>/applications/', JobApplicationsView.as_view(), name='job-applications'),

    # Employer → accept/reject application
    path('applications/<int:application_id>/status/', UpdateApplicationStatusView.as_view(), name='update-application-status'),
]