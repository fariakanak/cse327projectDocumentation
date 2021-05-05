from django.db import models

# Create your models here.
class User(models.Model):
    email_id = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length = 100, null=True)
    dob = models.DateTimeField(null=True)
    password = models.CharField(max_length = 250, null=True)
    works_in = models.ForeignKey('Dept', on_delete=models.CASCADE, null=True, blank=True)
    manager = models.EmailField(null=True, blank=True)
    has_uploaded = models.ForeignKey('Document', on_delete=models.CASCADE, null=True, blank=True)

    def upload_avatar(self, filename):
        path = 'hrm/avatar/{}'.format(filename)
        return path
    avatar = models.ImageField(upload_to=upload_avatar, null=True, blank=True)

    def __str__(self):
        return f"{self.email_id} - {self.name}"

class Dept(models.Model):
    dept_no = models.IntegerField(unique=True)
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.dept_name}"

class Document(models.Model):
    record_no = models.IntegerField(unique=True)
    record_name = models.CharField(max_length=250)
    archive_date = models.DateTimeField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def upload_document(self, filename):
        path = 'hrm/file/{}'.format(filename)
        return path
    file = models.FileField(upload_to=upload_document, null=True, blank=True)


    def __str__(self):
        return f"{self.record_no} - {self.record_name}"

class Team(models.Model):
    team_no = models.IntegerField(unique=True)
    members = models.EmailField()
    handles = models.ForeignKey(Document, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.team_no} - {self.handles_id}"
