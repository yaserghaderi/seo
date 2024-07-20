# myapp/views.py
from django.shortcuts import render, redirect
import tldextract

from .form import SimpleKeywordForm
from .models import linkofenemy, KeywordsFinals, Keyword,KeywordsRank,competitor
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

linksofenemies = []
results =[]

def firstSerp(keyword):
    def save_google_search_page(keyword, file_path):
        url = f"https://www.google.com/search?q={keyword}"
        response = requests.get(url)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

    file_path = "google_search_page.html"
    save_google_search_page(keyword, file_path)

    def scrape_and_save(html_file):
        with open(html_file, 'r', encoding='utf-8') as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, 'html.parser')

        related = soup.find_all('span', class_="Xe4YD")
        related_keywords = []

        for element in related:
            span = element.find('div')
            if span:
                related_keywords.append(span.get_text())

        links_serp = soup.find_all('div', class_="egMi0")

        links1 = []
        for element in links_serp:
            span = element.find('a')
            links = span.get('href')
            newlink = links.split('&')[0].replace('/url?q=', '')
            extracted = tldextract.extract(newlink)
            domain = f"{extracted.domain}.{extracted.suffix}"
            linksofenemies.append(domain)



        return related_keywords

    html_file = "google_search_page.html"
    related_keywords = scrape_and_save(html_file)

    return related_keywords


def search_view(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if keyword:
            related_keywords = firstSerp(keyword)
            for i in range(0, 5):
                list = firstSerp(related_keywords[i])
                for k in list:
                    related_keywords.append(k)
            related_keywords = remove_duplicates(related_keywords)
            # ذخیره کلمات کلیدی در دیتابیس
            for related_keyword in related_keywords:
                Keyword.objects.create(keyword=keyword, related_keyword=related_keyword)

            # ذخیره لینک در دیتابیس
            for links in linksofenemies:
                linkofenemy.objects.create(link=links)
            keywords = Keyword.objects.all()
            return render(request, 'myapp/saved_keywords.html', {'keywords': keywords})
    return render(request, 'myapp/search.html')


def saved_keywords_view(request):
    keywords = Keyword.objects.all()
    return render(request, 'myapp/saved_keywords.html', {'keywords': keywords})


def saved_links_view(request):
    links = linkofenemy.objects.all()
    domain_counts = defaultdict(lambda: {'count': 0, 'ids': []})

    for link in links:
        # استخراج URL از شیء linkofenemy
        url = link.link
        # استخراج دامنه از لینک
        extracted = tldextract.extract(url)
        domain = f"{extracted.domain}.{extracted.suffix}"
        # افزایش شمارش دامنه و افزودن id به لیست ids در دیکشنری
        domain_counts[domain]['count'] += 1
        domain_counts[domain]['ids'].append(link.id)

    # تبدیل دیکشنری به لیست از دیکشنری‌های کوچک و مرتب‌سازی بر اساس تعداد
    results = sorted(
        [{'link': domain, 'count': info['count'], 'ids': info['ids']} for domain, info in domain_counts.items()],
        key=lambda x: x['count'],
        reverse=True
    )



    return render(request, 'myapp/saved_links.html', {'links': results})


def save_selected_keywords(request):
    if request.method == 'POST':
        selected_keywords = request.POST.getlist('selected_keywords')
        for item in selected_keywords:
            KeywordsFinals.objects.create(field1=item)
        return redirect('search')


def remove_duplicates(realated_keywords):
    # تبدیل لیست به مجموعه برای حذف تکراری‌ها و سپس تبدیل مجدد به لیست
    return list(set(realated_keywords))


def home(request):
    return render(request, 'myapp/home.html')



def bulk_action(request):
    selected_keywords = request.POST.getlist('selected_keywords')
    action = request.POST.get('action')

    if action == 'delete-rank':
        KeywordsRank.objects.filter(id__in=selected_keywords).delete()
        return redirect('keyword_rank')

    elif action == 'delete-links':
        linkofenemy.objects.all().delete()
        return redirect('links')

    elif action == 'delete':
        Keyword.objects.filter(id__in=selected_keywords).delete()
        return redirect('keyword_list')
    elif action == 'transfer':
        transfer_keywords_to_rank_db(selected_keywords)
        return redirect('keyword_rank')

    elif action == 'add-competitor':
        transfer_links_to_db(selected_keywords)
        print(selected_keywords)
        return redirect('keyword_rank')

def transfer_links_to_db(keyword_ids):
    id=keyword_ids[0]
    print(id)
    keywords = linkofenemy.objects.filter(id__in=id)

    for keyword in keywords:
        competitor.objects.create(url=keyword)


def competitor_view(request):
    url = competitor.objects.all()
    return render(request, 'myapp/competitor.html', {'links': url})
def transfer_keywords_to_rank_db(keyword_ids):
    keywords = Keyword.objects.filter(id__in=keyword_ids)
    for keyword in keywords:
        KeywordsRank.objects.create(keyword=keyword)


def keyword_ranks(request):
    keyword = KeywordsRank.objects.all()
    return render(request, 'myapp/keyword_rank.html', {'keyword': keyword})


def add_keyword(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')

        if keyword:
            KeywordsRank.objects.create(keyword=keyword)
            return redirect('keyword_rank')  # تغییر مسیر به صفحه لیست کلمات

    keywords = KeywordsRank.objects.all()
    return render(request, 'myapp/keyword_rank.html', {'keywords': keywords})