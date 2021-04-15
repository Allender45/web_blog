from django.shortcuts import render


def home(request):
    news = [
        {
            'title': 'Наша первая статья',
            'text': 'Полный текст статьи',
            'date': '1 января 2021',
            'author': 'John Smith',
        },
        {
            'title': 'Наша Вторая статья',
            'text': 'Полный текст статьи',
            'date': '2 января 2021',
            'author': 'Will Smith',
        }
    ]
    context = {
        'news': news,
        'title': 'Главная страница',
    }
    return render(request, 'blog/home.html', context)


def contacts(request):
    return render(request, 'blog/contacts.html', {})

