from PIL import Image
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='_user_profile_picture')
    followers = models.ManyToManyField(User, blank=True, related_name='followers')

    def __str__(self):
        return f'--{self.user.username}--  Profile'

    def save(self, *args, **kwags):
        super().save( *args, **kwags)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
