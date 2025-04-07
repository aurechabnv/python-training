from django.contrib import admin

from blog.models import BlogPost, Category

# Register your models here.
# admin.site.register(BlogPost)
# admin.site.register(Category)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published', 'date','word_count',)
    empty_value_display = 'Inconnu'

    list_editable = ('title', 'published',)
    list_display_links = ('slug',)

    search_fields = ('title', 'slug',)
    list_filter = ('published', 'date',)

    autocomplete_fields = ('author',)
    filter_horizontal = ('category',)

    list_per_page = 20
