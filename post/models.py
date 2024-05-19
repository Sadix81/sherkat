from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.
def image(image):
    if not image.name.lower().endswith(('.png' , '.jpg' , '.jpeg')):
        raise ValidationError("Only PNG and JPG and JPEG files are allowed for the image.")

class Post(models.Model):
    title = models.CharField(max_length=255 , validators=[MaxLengthValidator(255)])
    description = models.CharField(max_length=255 , validators=[MaxLengthValidator(255)] , default='This Post hasnt any description')
    image = models.ImageField(upload_to='posts/', null=True , blank=True , validators=[image])
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def truncated_description(self):
        if len(self.truncated_description) > 100 :
            return self.description[:100] + "..."
        return self.description