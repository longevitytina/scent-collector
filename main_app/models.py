from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
# TIMES = (
#     ('M', 'Morning'),
#     ('A', 'Afternoon'),
#     ('E', 'Evening')
# )

EMOTIONS = (
    ('H', 'Happy'),
    ('S', 'Sad'),
    ('L', 'Laughter'),
    ('A', 'Angry')
)


class Power(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("power_detail", kwargs={"pk": self.id})


class Scent(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    characteristics = models.TextField(max_length=100)
    rating = models.IntegerField()
    powers = models.ManyToManyField(Power)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def smelt_for_today(self):
        return self.wafting_set.filter(date=date.today()).count() >= len(EMOTIONS)


class Wafting(models.Model):
    date = models.DateField('Smelling Date')
    # time = models.CharField(
    #     max_length=1,
    #     choices=TIMES,
    #     default=TIMES[0][0]
    # )
    emotion = models.CharField(
        max_length=1,
        choices=EMOTIONS,
        default=EMOTIONS[0][0],
    )
    scent = models.ForeignKey(Scent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_emotion_display()} on the {self.date}"

    class Meta:
        ordering = ['-date']
