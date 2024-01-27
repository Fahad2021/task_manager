from django.db import models

class Todoitem(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='todo_photos/', blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    label = models.CharField(max_length=50, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

