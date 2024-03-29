from django.db import models
from account.models import User

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(default='', null=False, blank=False, max_length=50)
    category = models.CharField(default='', null=False, blank=False, max_length=10)
    content = models.TextField(default='', null=False, blank=False)
    writer = models.ForeignKey('account.User', on_delete=models.CASCADE, default=User.objects.first().pk)
    write_time = models.DateField(auto_now=True)
    location = models.CharField(default='', null=False, blank=False, max_length=10)
    hashtag = models.CharField(default='', null=True, blank=True, max_length=10)
    count = models.PositiveIntegerField(default=0)
    like_user = models.ManyToManyField(User, related_name='like', blank=True)
    photo1 = models.ImageField(upload_to='',blank=True,)
    photo2 = models.ImageField(upload_to='',blank=True,)
    photo3 = models.ImageField(upload_to='',blank=True,)

    def count_like_user(self):  # total likes_user
        return self.like_user.count()

    #like_user 만들기
    def __str__(self):
        return self.writer_id


class Comment(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE,null=True,related_name='comments')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE,null=True)
    content = models.CharField(default='',null=True,max_length=200)
    created_dt = models.DateField(auto_now_add=True)
    updated_dt = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
