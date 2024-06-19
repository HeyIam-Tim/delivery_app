from django.db import models

from core.models.model_mixins import CreatedMixin, UpdatedMixin


class DeliveryPoint(CreatedMixin, UpdatedMixin, models.Model):
    """
        Пункт выдачи.

        owner_code:
            Принадлежность офиса компании:
            CDEK— офис принадлежит компании СДЭК
            Градусы — офис принадлежит компании Градусы
            Телепорт — офис принадлежит компании Телепорт
            Tastamat — офис принадлежит компании Tastamat
            Халва — офис принадлежит компании Халва
            PickPoint — офис принадлежит компании PickPoint
            OmniCDEK — офис принадлежит компании OmniCDEK
            OmniCDEK (franchise) — офис принадлежит компании OmniCDEK (франчайзи)
            OmniCDEK (self-employed) — офис принадлежит компании OmniCDEK (самозанятые)
            "Нет бренда" — офис принадлежит компании без бренда

        dimensions:
            Перечень максимальных размеров ячеек (только для type = POSTAMAT)
"""

    TYPES = (
        (0, 'NONE'),
        (1, 'CDEK'),
        (2, 'YANDEX'),
    )
    delivery_point_type = models.PositiveSmallIntegerField(verbose_name='Тип пункта выдачи', choices=TYPES, default=0)

    city = models.ForeignKey('core.City', verbose_name='Город', related_name='delivery_points', on_delete=models.SET_NULL, null=True, blank=True)

    code = models.CharField(verbose_name='Код пункта выдачи', unique=True, max_length=50, null=True, blank=True)

    uuid = models.CharField(verbose_name='Идентификатор пункта выдачи', unique=True, max_length=50, null=True, blank=True)

    name = models.CharField(verbose_name='Наименование', max_length=50, null=True, blank=True)

    address_comment = models.CharField(verbose_name='Описание местоположения', max_length=255, null=True, blank=True)

    nearest_station = models.CharField(verbose_name='Ближайшая станция/остановка транспорта', max_length=50, null=True, blank=True)

    work_time = models.CharField(verbose_name='Режим работы', max_length=100, null=True, blank=True)

    phones = models.CharField(verbose_name='Телефоны', max_length=255, null=True, blank=True)

    email = models.CharField(verbose_name='Адрес электронной почты', max_length=255, null=True, blank=True)

    type = models.CharField(verbose_name='Тип ПВЗ: PVZ — склад СДЭК, POSTAMAT — постамат СДЭК', max_length=8, null=True, blank=True)

    owner_code = models.CharField(verbose_name='Принадлежность офиса компании', max_length=255, null=True, blank=True)

    take_only = models.BooleanField(verbose_name='Является ли офис только пунктом выдачи или также осуществляет приём грузов', default=False, null=True, blank=True)

    is_handout = models.BooleanField(verbose_name='Является пунктом выдачи', default=False, null=True, blank=True)

    is_reception = models.BooleanField(verbose_name='Является пунктом приёма', default=False, null=True, blank=True)

    is_ltl = models.BooleanField(verbose_name='Работает ли офис с LTL (сборный груз)', default=False, null=True, blank=True)

    have_cashless = models.BooleanField(verbose_name='Есть безналичный расчет', default=False, null=True, blank=True)

    have_cash = models.BooleanField(verbose_name='Есть приём наличных', default=False, null=True, blank=True)

    allowed_cod = models.BooleanField(verbose_name='Разрешен наложенный платеж в ПВЗ', default=False, null=True, blank=True)

    weight_min = models.FloatField(verbose_name='Минимальный вес (в кг.), принимаемый в ПВЗ (> WeightMin)', default=0.0, null=True, blank=True)

    weight_max = models.FloatField(verbose_name='Максимальный вес (в кг.), принимаемый в ПВЗ (<=WeightMax)', default=30.0, null=True, blank=True)

    postamat_width = models.PositiveIntegerField(verbose_name='POSTAMAT Ширина (см)', null=True, blank=True)

    postamat_height = models.PositiveIntegerField(verbose_name='POSTAMAT Высота (см)', null=True, blank=True)

    postamat_depth = models.PositiveIntegerField(verbose_name='POSTAMAT Глубина (см)', null=True, blank=True)

    postal_code = models.PositiveIntegerField(verbose_name='Почтовый индекс города', null=True, blank=True)

    latitude = models.FloatField(verbose_name='Широта', null=True, blank=True)

    longitude = models.FloatField(verbose_name='Долгота', null=True, blank=True)

    address = models.CharField(verbose_name='Адрес (улица, дом, офис) в указанном городе', max_length=255, null=True, blank=True)

    address_full = models.CharField(verbose_name='Полный адрес с указанием страны, региона, города, и т.д.', max_length=255, null=True, blank=True)

    # ormder = models.OneToOneField('cart.Order', verbose_name='Заказ', null=True,
    #                              blank=True, on_delete=models.SET_NULL,
    #                              related_name='pickup_point')

    def __str__(self):
        return f'{self.name} - {self.address}'

    class Meta:
        verbose_name = 'Пункт выдачи'
        verbose_name_plural = 'Пункты выдачи'

    @property
    def phones_list(self) -> list:
        """Список с номерами"""

        phones_list = []
        phone_numbers_list = self.phones.split(',')
        for phone in phone_numbers_list:
            phones_list.append(phone)

        return phones_list
