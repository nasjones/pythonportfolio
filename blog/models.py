from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title, self.pub_date.strftime('%b %e, %Y, %I:%M')

    def summary(self):
        if len(self.body) > 100:
            return self.body[:100] + '...'
        return self.body

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y')
