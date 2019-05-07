from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


def upload_pic_to(instance, filename):
    return 'user_data/{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False)
    profile_picture = models.ImageField(
        default='default.jpg', upload_to=upload_pic_to)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=255, verbose_name="Present Address")

    nid = models.CharField(max_length=23, verbose_name="NID")
    nid_front = models.ImageField(verbose_name="NID Front Picture", upload_to=upload_pic_to)
    nid_back = models.ImageField(verbose_name="NID Back Picture", upload_to=upload_pic_to)
    nid_selfie = models.ImageField(
        verbose_name="Selfie With Holding Your NID", upload_to=upload_pic_to)
    utility = models.ImageField(verbose_name="NID", upload_to=upload_pic_to)

    is_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)    
    
    def __str__(self):
        return f'{self.user.username} Profile'

        def save(self, *args, **kwargs):
            super(Profile, self).save(*args, **kwargs)
            img = Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)
