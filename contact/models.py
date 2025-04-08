from django.db import models

class Contact(models.Model):
    CATEGORY_CHOICES = [
        ('customer', 'Customer'),
        ('prospect', 'Prospect'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

class CommunicationLog(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='logs')
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=[('email', 'Email'), ('call', 'Call'), ('meeting', 'Meeting')])
    notes = models.TextField()

    def __str__(self):
        return f"{self.type} with {self.contact.name} on {self.date}"
