from django.db import models

# Create your models here.
TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

EMOTIONS = (
    ('H', 'Happy'),
    ('S', 'Sad'),
    ('H', 'Humorous'),
    ('A', 'Angry')
)


class Scent(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    characteristics = models.TextField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Wafting(models.Model):
    date = models.DateField()
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    emotion = models.CharField(
        max_length=1,
        choices=EMOTIONS,
        default=EMOTIONS[0][0],
    )
    scent = models.ForeignKey(Scent, on_delete=models.CASCADE)

    def __str__(self):
        return f"This smell made you feel {self.get_emotion_display()} in the {self.get_time_display} on {self.date}"
