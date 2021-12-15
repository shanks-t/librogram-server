from django.db import models
from django.contrib.auth.models import User
from librogramapi.models.user_book import UserBook
from datetime import date



class ReadingGoal(models.Model):

    number_of_pages = models.IntegerField(null=True)
    number_of_books = models.IntegerField(null=True)
    start_date = models.DateField(default=date.today())
    end_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    @property
    def status(self):

        today = date.today()
        user_books = UserBook.objects.filter(user=self.user)
        completed_books = 0
        if self.end_date <= today:
            for book in user_books:
                if book.status.label == 'finished':
                    completed_books += 1
            
            if completed_books >= self.number_of_books:
                return "completed"
            else:
                return "incomplete"

        

#completed_pages = 0
# for goal in goals:
#     if goal.number_of_pages:
#         for book in user_books:
#             if book.finish_date:
#                 completed_pages += book.book.page_count

#             elif book.current_page:
#                 completed_pages += book.current_page
            
#             return completed_pages