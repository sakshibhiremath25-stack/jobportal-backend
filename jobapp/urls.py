from django.urls import path
from .views import (
    create_job,
    list_jobs,
    job_detail,
    update_job,
    delete_job
)

urlpatterns = [
    path('jobs/create/', create_job),
    path('jobs/', list_jobs),
    path('jobs/<int:pk>/', job_detail),
    path('jobs/<int:pk>/update/', update_job),
    path('jobs/<int:pk>/delete/', delete_job),
]