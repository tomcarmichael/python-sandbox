# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

from datetime import date

class Article:
    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def synopsis(self):
        return f'This is an article about {self.title} by {self.author}'
    
# Extend class

class WebArticle(Article):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posted_on = date.today()

    def get_posted_date(self):
        return f'This article was posted on {self.posted_on}'

my_article = Article('How to code in Python', "Guido van Rossum")

print(my_article.author)

print(my_article.synopsis())

my_web_article = WebArticle('Why you should use linux', 'Linus Torvalds')

print(my_web_article.get_posted_date())
print(my_web_article.synopsis())
