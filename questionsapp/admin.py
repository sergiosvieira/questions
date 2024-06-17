from django.contrib import admin

from django.contrib import admin
from .models import User, Question, Item, AnsweredQuestion

admin.site.register([
    User,
    Question,
    Item,
    AnsweredQuestion
])