# myapp/admin.py
from django.contrib import admin
from .models import Keyword, linkofenemy, KeywordsFinals,KeywordsRank


# Register your models here.
admin.site.register(Keyword)
admin.site.register(linkofenemy)
admin.site.register(KeywordsFinals)


def delete_all_keywords(modeladmin, request, queryset):
    Keyword.objects.all().delete()

delete_all_keywords.short_description = "Delete all keywords"


try:
    admin.site.unregister(Keyword)
except admin.sites.NotRegistered:
    pass


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'related_keyword')
    actions = [delete_all_keywords]


class KeywordsRankAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'Mysite', 'myrank', 'rank_comparator1', 'rank_comparator2')

admin.site.register(KeywordsRank, KeywordsRankAdmin)