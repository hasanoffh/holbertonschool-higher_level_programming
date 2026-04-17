#!/usr/bin/python3
"""
JSONPlaceholder API-dan məlumat çəkmək və emal etmək üçün skript.
"""
import requests
import csv


def fetch_and_print_posts():
    """Bütün postları çəkir və başlıqlarını çap edir."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))

    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Postları çəkir və posts.csv faylına yadda saxlayır."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)

    if r.status_code == 200:
        posts = r.json()
        # Lazımi sahələri seçərək lüğət siyahısı yaradırıq
        data_to_save = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
