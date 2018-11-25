from django.db import models



class User(models.Model):
  username  = models.CharField(max_length=264, unique=True)
  email     = models.EmailField()

  def __str__(self):
    return self.name



class Tweet(models.Model):
  text = models.CharField(max_length=140)
  date = models.DateField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.text