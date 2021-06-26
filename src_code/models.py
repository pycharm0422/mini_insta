from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to ='media/% Y/% m/% d/',null=True, blank=True)
    post = models.TextField(null=True, blank=False)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    tag = models.ManyToManyField(User, related_name='tags', blank=True)
    saved = models.ManyToManyField(User, related_name='saved', blank=True)

    def __str__(self):
        return str(self.pk) + " Post"

    def get_likes_count(self):
        return self.likes.count




class Message(models.Model):
    # sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    sender = models.CharField(max_length=300, null=True, blank=True)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=False)
    
    def __str__(self):
        return self.sender + " has send message to " + self.receiver.username

class Room(models.Model):
    room_name = models.CharField(max_length=200, null=True)
    message = models.ManyToManyField(Message, related_name='messages', blank=True)

    def __str__(self):
        return self.room_name


class Detail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default_pic.jpg', upload_to ='media/% Y/% m/% d/',null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)


    def __str__(self):
        return self.name


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.user.username + " comment"
