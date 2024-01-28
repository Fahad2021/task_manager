from django.db import models
from django.utils import timezone
from django.urls import reverse

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    def __str__(self):
        return self.title

   
class ToDoItem(models.Model):
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

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )
    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]


    

