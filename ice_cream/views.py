from django.shortcuts import render

ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир — это не надолго.',
        'price': 150,
        'category': {'title': 'Пломбир'},
        'toppings': []
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
        'price': 250,
        'category': {'title': 'Экзотическое'},
        'toppings': [
            {'title': 'Карамель'},
            {'title': 'Шоколадная крошка'}
        ]
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
        'price': 200,
        'category': {'title': 'Необычное'},
        'toppings': [
            {'title': 'Соленая карамель'}
        ]
    },
]


def ice_cream_list(request):
    """Отображает список всего мороженого"""
    return render(request, 'ice_cream/list.html', {'ice_creams': ice_cream_catalog})


def ice_cream_detail(request, pk):
    """Отображает детальную информацию о конкретном мороженом"""
    template = 'ice_cream/detail.html'
    context = {'ice_cream': ice_cream_catalog[pk]}
    return render(request, template, context)
