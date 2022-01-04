from django.db import models
from django.contrib.auth.models import User
from librogramapi.models.user_book import UserBook
from datetime import date



class ReadingGoal(models.Model):

    number_of_pages = models.IntegerField(null=True)
    number_of_books = models.IntegerField(null=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    @property
    def status(self):

        today = date.today()
        goal_date = self.end_date
        user_books = UserBook.objects.filter(user=self.user)
        completed_books = 0
        for book in user_books:
            if book.status and self.number_of_books:
                if book.status.label == 'finished':
                    completed_books += 1
        if completed_books:
            progress = round((completed_books/self.number_of_books * 100), 2)
            if progress > 100:
                progress = 100
                return progress
            elif goal_date >= today:
                return progress
            elif goal_date < today:
                return f'expired  {progress}'
        else:
            return 0
    
        

#completed_pages = 0
# for goal in goals:
#     if goal.number_of_pages:
#         for book in user_books:
#             if book.finish_date:
#                 completed_pages += book.book.page_count

#             elif book.current_page:
#                 completed_pages += book.current_page
            
#             return completed_pages