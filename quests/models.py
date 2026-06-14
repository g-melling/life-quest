from django.db import models

class Quest(models.Model):
    title = models.CharField(max_length=200)
    xp_reward = models.IntegerField(default=10)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title