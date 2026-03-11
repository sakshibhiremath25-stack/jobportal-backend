from django.urls import path
from .views import (
    JobListView,
    ApplyJobView,
    MyApplicationsView,
    JobApplicationsView,
    create_job,
    list_jobs,
    job_detail,
    update_job,
    delete_job
)

urlpatterns = [
    # Job CRUD APIs
    path('jobs/create/', create_job, name='create-job'),
    path('jobs/', list_jobs, name='list-jobs'),
    path('jobs/<int:pk>/', job_detail, name='job-detail'),
    path('jobs/<int:pk>/update/', update_job, name='update-job'),
    path('jobs/<int:pk>/delete/', delete_job, name='delete-job'),

    # Job list using DRF
    path('jobs/list/', JobListView.as_view(), name='job-list'),

    # Apply for job
    path('jobs/<int:job_id>/apply/', ApplyJobView.as_view(), name='apply-job'),

    # Candidate view applied jobs
    path('my-applications/', MyApplicationsView.as_view(), name='my-applications'),

    # Recruiter view applications for a job
    path('jobs/<int:job_id>/applications/', JobApplicationsView.as_view(), name='job-applications'),
]