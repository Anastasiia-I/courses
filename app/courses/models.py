from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=300)
    img_path = models.CharField(max_length=300)

class Course(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    logo = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Contact(models.Model):
    TYPE = (
        (1, 'Phone'),
        (2, 'Facebook'),
        (3, 'Email'),
    )
    type = models.IntegerField(choices=TYPE)
    value = models.CharField(max_length=300)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

class Branch(models.Model):
    address = models.CharField(max_length=300)
    latitude = models.CharField(max_length=300)
    longitude = models.CharField(max_length=300)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)






