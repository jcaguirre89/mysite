from django.contrib import admin

from .models import Question, Choice
# Register your models here.

#Register Questions model for admin site
#first set up class with desired available fields, then register it.
  
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
"""
this version shows each choice stacked on each other
class ChoiceInline(admin.StackedInline):
    model = Choice
    #How many default choices to include
    extra = 3
"""

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'],
                          'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
"""
this version doesn't separate fields into different blocks

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text'] 
    
"""

admin.site.register(Question, QuestionAdmin)

