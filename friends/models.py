from django.db import models
from django.contrib.auth.models import User

class Friendship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boss')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    groupname=models.CharField(max_length=100,blank=True)
    class Meta:
        unique_together = ['user', 'friend']

    def __str__(self):
        return f"{self.user} - {self.friend}"
class FriendRequest(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender")
    receipient=models.ForeignKey(User,on_delete=models.CASCADE,related_name="receiver")
    date=models.DateTimeField(auto_now_add=True)
    accepted=models.BooleanField(default=False)
    declined=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.sender} {self.receipient} {self.date}"
class Chat(models.Model):
    cotent=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    group=models.CharField(max_length=100)
