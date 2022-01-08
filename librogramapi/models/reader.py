from django.db import models
from django.contrib.auth.models import User
from librogramapi.models.user_book import UserBook
from librogramapi.models.reading_goal import ReadingGoal, UserBook


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=70)
    profile_image_url = models.URLField()
    subscriber = models.BooleanField(default=False)


    @property
    def current_books(self): 
        books = UserBook.objects.filter(user=self.user)
        total = len(books)
        
        return total
    
    @property
    def goals(self):
        goals = ReadingGoal.objects.filter(user=self.user)
        total = len(goals)
        
        return total