from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone
# Create your models here.

class Participant(models.Model):
    #participant_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length = 20)
    email = models.EmailField(max_length=50)
    #address = models.ForeignKey('Address', on_delete=models.CASCADE, blank=True, null=True) #automatically inserts _id at end of ForeignKey
    address = models.CharField(max_length=50, null = True)
    address2 = models.CharField(max_length=50, blank=True, null = True)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    comments = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return f'{self.last_name}, {self.first_name}, {self.email}, {self.address}, {self.city}, {self.country}'

    #def report_view(self, request):
    #    data = (self.user_report(user) for user in User.objects.all().order_by('first_name'))
    #    context = {'report': json.dumps(list(data))}
    #    return HttpResponse(render(request,
    #                           'admin/users_report.html',
    #                           context),
    #                    content_type='text/html')

class Meta:
    #managed = False
    db_table = 'participant'


class Portal_user(models.Model):

     #Create relationship (don't inherit from User!)
    #user = models.OneToOneField(User, on_delete=None)

    username = models.CharField(max_length=50, unique = True)
    email = models.EmailField(max_length=50, unique = True)
    password = models.CharField(max_length = 100)
    password2 = models.CharField(max_length = 100)

    def __str__(self):
        return self.username + " " + self.email + " " +self.password

class Meta:
    #managed = False
    db_table = 'portal_user'

'''
class Address(models.Model):
    #address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null = True)
    postal_code = models.CharField(max_length=10)
    #participant = models.ForeignKey('Participant', models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey('City',on_delete=models.CASCADE, blank=True, null=True)
    #participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    class Meta:
        #managed = False  --this allows Django to create, modify and delete table
        db_table = 'address'


class City(models.Model):
    #city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'city'


class Country(models.Model):
    #country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)

    class Meta:
        #managed = False
        db_table = 'country'
# Create your models here.
'''
