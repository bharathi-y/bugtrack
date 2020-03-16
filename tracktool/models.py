
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.core.validators  import *



class Bugs(models.Model):
    prioritychoice = (
        ('1', 'priority and important'),
        ('2', 'picked in resolved in 60 min time'),
        ('3', 'picked in 2 hrs'),
        ('4', 'picked in 12 hrs'),
        ('5', '24 hrs priority'),
    )
    issues=(('sl','software relate'),
            ('hw','hardware relate'),
            ('Nw','Network relate')
            )
    statschoice=(('op','open'),
                 ('as','assigned'),
                 ('INP','Inprogress'),
                 ('cl','closed'),
                 ('fw','changedepartment')
                 )
    name=models.ForeignKey(User,help_text= 'User liked the post',on_delete=models.CASCADE)
    priority=models.CharField(max_length=2,help_text='1 is most prioritised',choices=prioritychoice)
    issue=models.CharField(max_length=50,help_text='select related',choices=issues)
    discription=models.TextField(max_length=300,help_text='elaberate the issue')
    status=models.CharField(max_length=3,help_text='status',choices=statschoice)
    attachments=models.ImageField(upload_to="images/",blank=True,null=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "(0) - {1}".format(self.name,self.priority,self.issue,self.status)