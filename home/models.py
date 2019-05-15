from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from post.models import post

# Create your models here.
class HomePost(models.Model):
     title=models.CharField(max_length=120)
     user = models.ForeignKey(User,
            on_delete=models.CASCADE)
     katilimci=models.ManyToManyField(User, related_name='katilimci', blank=True)
     content=models.TextField()
     publishing_date=models.DateTimeField(auto_now_add=True)
     image=models.FileField(null=True,blank=True)

     def __str__(self):
         return self.title
     def get_absolute_url1(self):
         return reverse('home:katil',kwargs={'id':self.id})


     class Meta:
         ordering=['-publishing_date']
class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True,on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)


