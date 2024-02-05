from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
}


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Рецепт омлета': reverse('omlet'),
        'Рецепт макарошек': reverse('pasta'),
        'Рецепт вкуснячего бутера': reverse('buter')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def buter_view(request):
    template_name = 'calculator/index.html'
    pages = {
        'Вернуться на главную страницу': reverse('home')
    }
    context = {
        'recipe': {
        },
        'pages': pages
    }
    servings = int(request.GET.get('servings', 1))
    context['servings'] = servings
    for ing in DATA['buter']:
        quantity = round(float(DATA['buter'][ing] * servings), 2)
        context['recipe'].update({ing: quantity})
    return render(request, template_name, context)


def omlet_view(request):
    template_name = 'calculator/index.html'
    pages = {
        'Вернуться на главную страницу': reverse('home')
    }
    context = {
        'recipe': {
        },
        'pages': pages
    }
    servings = int(request.GET.get('servings', 1))
    context['servings'] = servings
    for ing in DATA['omlet']:
        quantity = round(float(DATA['omlet'][ing] * servings), 2)
        context['recipe'].update({ing: quantity})
    return render(request, template_name, context)


def pasta_view(request):
    template_name = 'calculator/index.html'
    pages = {
        'Вернуться на главную страницу': reverse('home')
    }
    context = {
        'recipe': {
        },
        'pages': pages
    }
    servings = int(request.GET.get('servings', 1))
    context['servings'] = servings
    for ing in DATA['pasta']:
        quantity = round(float(DATA['pasta'][ing] * servings), 2)
        context['recipe'].update({ing: quantity})
    return render(request, template_name, context)
