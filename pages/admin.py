from django.contrib import admin
from .models import *

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]




class TimelineInLine(admin.TabularInline):
    model = Timeline
    extra = 1

class TimelineAdmin(admin.ModelAdmin):
    inlines = [TimelineInLine]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Image)
admin.site.register(ContactMessage)
admin.site.register(Timeline_category, TimelineAdmin)
admin.site.register(Timeline)
admin.site.register(About_description)
admin.site.register(About_blog_1)
admin.site.register(About_blog_2)
admin.site.register(About_title_1)
admin.site.register(About_title_2)
admin.site.register(About_title_3)
