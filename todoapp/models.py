from django.db import models

# Create your models here.
PRI = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))
class TodoModel(models.Model):
  title = models.CharField(max_length=100)
  memo = models.TextField()
  priority = models.CharField(
      max_length = 10,
      choices = PRI
  )
  duedate = models.DateField()
  def __str__(self):
    return self.title