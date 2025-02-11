from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=55)
    lastname = models.CharField(max_length=55)
    image = models.ImageField(upload_to="Author")
    othername = models.CharField(max_length=55, blank=True, null=True)
    email = models.EmailField()
    phone_number_1 = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.firstname