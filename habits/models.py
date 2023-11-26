from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)  # e.g., 'Active', 'Completed'
    streak_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class HabitJournal(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    note = models.TextField()


# Notifications and Reminders
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    notification_time = models.DateTimeField()
    seen = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username} at {self.notification_time}"


# Community Engagement
class CommunityPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user.username}"


# Resource Center
class Resource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    author = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


# Additional Features
class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50)  # e.g., 'Light', 'Dark'
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"Settings for {self.user.username}"


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback from {self.user.username}"
