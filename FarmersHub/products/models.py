from django.db import models

# model for iteams.
class product(models.Model):
  LIVE=1
  DELETE=0
  DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
  title=models.CharField(max_length=200)
  price=models.FloatField()
  description=models.TextField()
  image=models.ImageField(upload_to='media/')
  priority=models.IntegerField(default=0)
  created_at=models.DateTimeField(auto_now_add=True)
  updaed_at=models.DateTimeField(auto_now=True)



  def __str__(self):
    return self.title 