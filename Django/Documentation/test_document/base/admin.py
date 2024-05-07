from django.contrib import admin
from .models import *


class ChoiceInline(admin.TabularInline): # In side format like table and StackedInline makes it simple format.
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {"fields":["question_text"]}),
        (
            "Date information", {"fields":["pub_date"],
            "classes":["collapse"]}
            )
        ]
    inlines=[ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter=['pub_date']
    search_fields=["question_text"]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

admin.site.register(School)
admin.site.register(Student)
