from django.db import models
from jsonfield import JSONField


class Participant(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Question(models.Model):
    title = models.CharField(max_length=1000)
    is_multiple = models.BooleanField(default=False)
    is_mandatory = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Choises(models.Model):
    question = models.ForeignKey(Question,on_delete=models.PROTECT)
    choice = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice


class Result(models.Model):
    participant = models.ForeignKey(Participant,on_delete=models.PROTECT)
    question = models.ForeignKey(Question,on_delete=models.PROTECT)
    answer = models.ForeignKey(Choises,on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




    

    



    
