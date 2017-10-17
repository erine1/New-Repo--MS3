from django.db import models

class Book_Series(models.Model):
    book_author = models.CharField(max_length = 250)
    book_title = models.CharField(max_length = 500)

    def _str_(self):
        return self.book_title + ' - ' + self.book_author


class Title(models.Model):
    Book_Series = models.ForeignKey(Book_Series, on_delete= models.CASCADE)
    file_type = models.CharField(max_length = 10)
    book_title = models.CharField(max_length = 250)
