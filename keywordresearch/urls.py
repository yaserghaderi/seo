from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('keywords/', views.saved_keywords_view, name='keyword_list'),
    path('links/', views.saved_links_view, name='links'),
    path('save_selected_keywords/', views.save_selected_keywords, name='save_selected_keywords'),
    path('', views.home),
    path('bulk_action/', views.bulk_action, name='bulk_action'),
    path('keyword_rank/', views.keyword_ranks, name='keyword_rank'),
    path('add_keyword/', views.add_keyword, name='add_keyword'),
    path('competitor/', views.competitor_view, name='competitor'),
]
