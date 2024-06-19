from django.conf import settings

LOGGER = settings.LOGGER


class FacadeBaseDeliveryCdek:
    """Базовый фасад для СДЕК"""

    def get_cdek_city_code(self, city_id: str) -> dict:
        """Получает id города для СДЕК"""

        from core.service.facades import FacadeCity

        cdek_city_code_data = {}

        city = FacadeCity.get_city_by_id(city_id=int(city_id))
        if not city:
            cdek_city_code_data = {
                'cdek_city_code': None,
                'errors': [f'Нет города с id: {city_id}'],
            }
            return cdek_city_code_data

        if not city.cdek_city_code:
            message = f'Не найден cdek_city_code; Город: {city}'

            cdek_city_code_data = {
                'cdek_city_code': None,
                'errors': [message],
            }

            LOGGER.warning(message)

            return cdek_city_code_data

        cdek_city_code_data = {
            'cdek_city_code': city.cdek_city_code,
            'errors': [],
        }
        return cdek_city_code_data
