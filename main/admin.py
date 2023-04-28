from django.contrib import admin
from main.models import *

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizResult)

# Register your models here.
