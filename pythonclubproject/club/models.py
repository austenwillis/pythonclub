from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#product type, product, review

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.CharField(max_length=255)
    agenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meeting=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)

    meetingtext=models.TextField()
    
    
    def __str__(self):
        return str(self.meeting)

    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedesciption=models.TextField()



    def __str__(self):
        return self.resourcename

        
    class Meta:
        db_table='resource'


class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdesciption=models.TextField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    

    class Meta:
        db_table='event'