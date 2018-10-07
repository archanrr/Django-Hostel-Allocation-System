from django.db import models

class Register(models.Model):
    username_login=models.CharField(max_length=20)
    password_login=models.CharField(max_length=20)
    def _str_(self):
        return self.name

class hostel(models.Model):
    #hostelid=models.IntegerField(max_length=3)
    warden=models.CharField(max_length=20)
    no_of_rooms=models.IntegerField()

    def _str_(self):
        return self.name

class rooms(models.Model):
    hostelid=models.ForeignKey('hostel',on_delete=models.CASCADE)
    dept=models.CharField(max_length=4)
    no_of_students=models.IntegerField()

    def _str_(self):
        return self.name


class Students(models.Model):
    roomid=models.ForeignKey('rooms',on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    dept=models.CharField(max_length=3)
    year=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()

    def _str_(self):
        return self.name