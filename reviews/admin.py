from django.contrib import admin
from reviews.models import Review

class Review_Admin(admin.ModelAdmin):
    list_display = ('stars', )

admin.site.register(Review, Review_Admin)
