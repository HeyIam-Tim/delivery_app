from django.conf import settings

LOGGER = settings.LOGGER


class DeliveryInterface():
    """Доставка интерфейс"""

    delivery_point_type: int = 0

    success_status = 'success'
    error_status = 'error'

    def form_response(self, *args, **kwargs) -> dict:
        """Формирует ответ"""

        raise NotImplementedError


class DeliveryCreateInterface:
    """Создание заказа интерфейс"""

    success_status = 'success'
    error_status = 'error'

    def form_response(self, *args, **kwargs) -> dict:
        """Формирует ответ"""

        raise NotImplementedError

    def delivery_create(self, *args, **kwargs) -> dict:
        """Создает заказ"""

        raise NotImplementedError


class DeliveryStatusInterface:
    """Получение статуса заказа интерфейс"""

    success_status = 'success'
    error_status = 'error'

    def form_response(self, *args, **kwargs) -> dict:
        """Формирует ответ"""

        raise NotImplementedError

    def delivery_status(self, *args, **kwargs) -> dict:
        """Получет статус заказа"""

        raise NotImplementedError


class DeliveryCancelInterface:
    """Отмена заказа интерфейс"""

    success_status = 'success'
    error_status = 'error'

    def form_response(self, *args, **kwargs) -> dict:
        """Формирует ответ"""

        raise NotImplementedError

    def delivery_cancel(self, *args, **kwargs) -> dict:
        """Отменяет заказа"""

        raise NotImplementedError


class DeliveryReturnInterface:
    """Возврат заказа интерфейс"""

    success_status = 'success'
    error_status = 'error'

    def form_response(self, *args, **kwargs) -> dict:
        """Формирует ответ"""

        raise NotImplementedError

    def delivery_return(self, *args, **kwargs) -> dict:
        """Создает возврат заказа"""

        raise NotImplementedError


class DeliveryIntakeInterface:
    """Вызов курьера интерфейс"""

    success_status = 'success'
    error_status = 'error'

    def form_response(self, *args, **kwargs) -> dict:
        """Формирует ответ"""

        raise NotImplementedError

    def delivery_intake(self, *args, **kwargs) -> dict:
        """Создает вызов курьера"""

        raise NotImplementedError


class DeliveryPointsInterface(DeliveryInterface):
    """Пункты выдачи интерфейс"""

    def get_delivery_points(self, *args, **kwargs) -> dict:
        """Получает пункты выдачи"""

        raise NotImplementedError


class DeliveryCalculatorInterface(DeliveryInterface):
    """Расчет доставки интерфейс"""

    def calculate(self, *args, **kwargs) -> dict:
        """Для расчета стоимости и сроков доставки"""

        raise NotImplementedError


class FacadeInterface():
    """Фасад интерфейс"""

    pass
