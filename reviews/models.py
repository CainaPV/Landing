from django.db import models

CHOICE_STARS = ((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars') )

class Review(models.Model):
    stars = models.IntegerField(choices=CHOICE_STARS, blank=True)
    
    def __str__(self):
        return str(self.stars)
