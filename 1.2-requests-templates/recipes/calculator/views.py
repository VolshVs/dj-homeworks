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
        'Рецепт омлета': 'http://127.0.0.1:8000/omlet/',
        'Рецепт макарошек': 'http://127.0.0.1:8000/pasta/',
        'Рецепт вкуснячего бутера': 'http://127.0.0.1:8000/buter/'
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def dish(request, dish):
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
    for ing in DATA[f'{dish}']:
        quantity = round(float(DATA[f'{dish}'][ing] * servings), 2)
        context['recipe'].update({ing: quantity})
    return render(request, template_name, context)
