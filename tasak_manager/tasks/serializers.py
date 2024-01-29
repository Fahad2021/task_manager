from rest_framework import serializers
from tasks.models import ToDoItem

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('title','description','photo','date_time','due_date','priority','label','complete')
