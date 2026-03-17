from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class ScreeningQuestion(models.Model):
    job = models.ForeignKey('Job', on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()

    def __str__(self):
        return self.question_text


class CandidateAnswer(models.Model):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(ScreeningQuestion, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f"{self.candidate} - {self.question}"
    
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.IntegerField()
    employer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, default="pending")
    applied_at = models.DateTimeField(auto_now_add=True)