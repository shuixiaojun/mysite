from django.utils.translation import ngettext
from django.contrib import admin, messages
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently', 'status')
    list_filter = ['pub_date', 'question_text', 'status']
    search_fields = ['question_text']
    fieldsets = [
        (None,               {'fields':['question_text', 'status']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    actions = ['make_published']
    def make_published(self, request, queryset):
        updated = queryset.update(status='2')
        self.message_user(request, ngettext(
            '%d question was successfully marked as published.',
            '%d questions were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = "批量改成发布"

admin.site.register(Question, QuestionAdmin)
