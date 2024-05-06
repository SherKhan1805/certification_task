from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from hierarchy.models import Contacts, Products, Factory, Retail, Entrepreneur


def clear_debt_action(modeladmin, request, queryset):

    # Применяем действие к каждому выбранному объекту
    for obj in queryset:
        obj.debt = 0
        obj.save()
    clear_debt_action.short_description = "Очистить задолженность"


@admin.register(Contacts)
class MovieAdmin(admin.ModelAdmin):
    # list_display = ("title", "category", "url", "draft")
    list_filter = ("city",)


class ContactCityFilter(admin.SimpleListFilter):
    title = 'City'

    parameter_name = 'city'

    def lookups(self, request, model_admin):
        cities = set(Contacts.objects.values_list('city', flat=True))
        return [(city, city) for city in cities]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contacts__city=self.value())


@admin.register(Factory)
class MovieAdmin(admin.ModelAdmin):
    list_filter = (ContactCityFilter,)


@admin.register(Retail)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contacts', 'products',
        'get_provider_from_factory_link',
        'debt', 'created_date'
    )

    list_display_links = ('get_provider_from_factory_link', 'name')

    list_filter = (ContactCityFilter,)

    def get_provider_from_factory_link(self, obj):
        # Получаем объект завода для данной торговой сети
        factory = obj.provider_from_factory

        # Создаем ссылку на страницу завода, используя его ID
        if factory:
            link = reverse("admin:hierarchy_factory_change", args=[factory.pk])
            return format_html('<a href="{}">{}</a>', link, factory)
        else:
            return "No Factory"

    get_provider_from_factory_link.short_description = "Ссылка на завод поставщик"

    actions = [clear_debt_action]


@admin.register(Entrepreneur)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contacts', 'products',
        'get_provider_link',
        'debt', 'created_date'
    )

    list_display_links = ('get_provider_link', 'name')

    list_filter = (ContactCityFilter,)

    def get_provider_link(self, obj):
        # Получаем объект завода для данной торговой сети
        if obj.provider_from_factory:
            factory = obj.provider_from_factory

            # Создаем ссылку на страницу завода, используя его ID
            link = reverse("admin:hierarchy_factory_change", args=[factory.pk])
            return format_html('<a href="{}">{}</a>', link, factory)

        elif obj.provider_from_retailer:
            retailer = obj.provider_from_retailer

            # Создаем ссылку на страницу завода, используя его ID
            link = reverse("admin:hierarchy_retail_change", args=[retailer.pk])
            return format_html('<a href="{}">{}</a>', link, retailer)

    get_provider_link.short_description = "Поставщик"

    actions = [clear_debt_action]


admin.site.register(Products)

