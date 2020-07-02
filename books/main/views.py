from django.shortcuts import render
from main.models import Book, Author, Category

def all_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()
    price_less_than_15 = Book.objects.filter(price__lte=15)
    authors_in_20th_century = Author.objects.filter(date_of_birthday__year__gte=1900,date_of_birthday__year__lte=2000)
    books_title_contains_a = Book.objects.filter(title__icontains="a")
    category_title_contains_a = Category.objects.filter(title__icontains="a")
    author_object_exactly_DanielDefoe = Author.objects.filter(fullname__iexact='Daniel Defoe')
    author_nationality_not_British = Author.objects.exclude(nationality__iexact='British')
    books_which_authors_name_start_D = Book.objects.filter(author__fullname__startswith='D')
    books_which_authors_gender_male = Book.objects.filter(author__gender='mr')
    books_which_category_title_end_e = Book.objects.filter(category__title__endswith='e')
    category_which_not_related_book = Category.objects.filter(books__isnull=True)
    book_which_primary_key_equal_3 = Book.objects.filter(pk=3)
    context = {
        'books' : books,
        'authors' : authors,
        'categories' : categories,
        'price_less_than_15' : price_less_than_15,
        'authors_in_20th_century' : authors_in_20th_century,
        'books_title_contains_a' : books_title_contains_a,
        'category_title_contains_a' : category_title_contains_a,
        'author_object_exactly_DanielDefoe' : author_object_exactly_DanielDefoe,
        'author_nationality_not_British' : author_nationality_not_British,
        'books_which_authors_name_start_D' : books_which_authors_name_start_D,
        'books_which_authors_gender_male' : books_which_authors_gender_male,
        'books_which_category_title_end_e' : books_which_category_title_end_e,
        'category_which_not_related_book' : category_which_not_related_book,
        'book_which_primary_key_equal_3' : book_which_primary_key_equal_3
    }
    return render(request,'index.html',context)

# Create your views here.
