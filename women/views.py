from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''Анджели́на Джоли́[4] (англ. Angelina Jolie[5], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.

Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая награду) и двух «Премий Гильдии киноактёров США».

Дебютировала в кино в 1982 году, сыграв роль в комедийном фильме «В поисках выхода» (где снимались также её отец и мать)[6], однако известность получила после того, как сыграла героиню видеоигр Лару Крофт в фильмах «Лара Крофт: Расхитительница гробниц» и «Лара Крофт: Расхитительница гробниц 2 — Колыбель жизни».

В 2009, 2011 и 2013 годах по версии журнала Forbes Джоли была названа самой высокооплачиваемой актрисой Голливуда[7][8].

Её наиболее успешными с коммерческой стороны фильмами стали «Малефисента» (сборы в мировом прокате — 758 миллионов долларов США), «Мистер и миссис Смит» (сборы в мировом прокате — 478 миллионов), «Особо опасен» (341 миллион), «Солт» (293 миллиона ), а также «Турист» (278 миллионов), «Лара Крофт: Расхитительница гробниц» (274 миллиона) и картина с участием Николаса Кейджа «Угнать за 60 секунд» (237 миллионов долларов США)[9]. ''',
     'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_catogory(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена.</h1>")
