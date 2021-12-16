from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
    def __str__(self):
        return self.name
class Books(models.Model):
    name = models.CharField(max_length=200,verbose_name='Название книги')
    yaer = models.CharField(max_length=4, verbose_name='Год выпуска книги')
    descrip = models.TextField( verbose_name='Краткое содержание книги')
    author = models.CharField(max_length=200, verbose_name='Автор книги')
    image = models.ImageField(upload_to='images')
    book_file = models.FileField(upload_to='books')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        null=True,
    )

    class Meta:
        verbose_name = 'Книжка'
        verbose_name_plural = 'Книги'
    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Books, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Комментарий")
    name = models.CharField(max_length=100, verbose_name="Имя")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text

class Search(models.Model):
    text = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Поиск'
    def __str__(self):
        return self.text

# class NewsLetter(models.Model):
#     email = models.EmailField(max_length=254)
#
#     class Meta:
#         verbose_name = "email"
#         verbose_name_plural = "emails"
#
#     def __str__(self):
#         return self.email