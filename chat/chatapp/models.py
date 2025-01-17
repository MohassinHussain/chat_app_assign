from django.db import models

# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return "User " + self.name

class Message(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='received_messages') #delete is required argument, cascade is just a kind of delete
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)