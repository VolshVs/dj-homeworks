from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_dict = {
        "name": 'name',
        "min_price": 'price',
        "max_price": "-price"
    }
    phones = Phone.objects.all()
    page_status = request.GET.get('sort', '')
    if page_status:
        phones = phones.order_by(sort_dict[page_status])
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)


# Комментарий преподавателя:

# "Единственное что хотелось бы добавить к основному заданию: скрипт загрузки данных можно сократить"
#
#  for phone in phones:
#             # TODO: Добавьте сохранение модели
#             pass
#             phone_object = Phone(**phone)
#             phone_object.save()

