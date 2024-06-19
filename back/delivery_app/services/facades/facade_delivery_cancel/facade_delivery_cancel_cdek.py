from django.conf import settings

from delivery_app.services.utils.interfaces import FacadeInterface

LOGGER = settings.LOGGER


class FacadeDeliveryCancelCdek(FacadeInterface):
    """Фасад для отмены заказа"""

    pass
