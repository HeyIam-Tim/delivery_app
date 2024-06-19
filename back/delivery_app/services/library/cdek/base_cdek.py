from typing import Optional
import requests

from django.conf import settings

LOGGER = settings.LOGGER


class BaseCdek():
    """СДЕК | Базовый класс"""

    client_id = settings.CDEK_CLIENT_ID
    client_secret = settings.CDEK_CLIENT_SECRET
    cdek_base_url = "https://api.cdek.ru/v2"  # боевой сервер
    # cdek_base_url = "https://api.edu.cdek.ru/v2"  # тестовый сервер
    cdek_auth_token: str = ""

    def request_to_cdek(self, method: str, url: str, params=None, headers: Optional[dict] = None,
                        data: Optional[dict] = None, retry=True) -> dict:
        if not headers:
            headers = {}

        request_methods = {
            "post": requests.post,
            "get": requests.get,
            "put": requests.put,
            "patch": requests.patch,
            "delete": requests.delete
        }
        request_method = request_methods.get(method.lower())
        headers['Authorization'] = self.cdek_auth_token or self.cdek_authorize()
        if request_method:
            response = request_method(url=url, json=data, headers=headers, params=params)
        else:
            raise Exception("Requested HTTP method is not supported")
        if response.ok:
            return {"status": self.success_status, "result": response.json()}
        # Если проблема с токеном, пытаемся получить новый и повторить запрос
        elif response.status_code == 401 and retry and response.json().get('requests')[0].get('type') == 'AUTH':
            headers['Authorization'] = self.cdek_auth_token or self.cdek_authorize()
            return self.request_to_cdek(method, url, params, headers, data, retry=False)
        else:
            try:
                errors = response.json().get('errors')
                if response.json().get('requests'):
                    errors = response.json().get('requests')[0].get('errors')
            except Exception:
                errors = response.text
            return {"errors": errors, "status": self.error_status}

    def cdek_authorize(self):
        url = f"{self.cdek_base_url}/oauth/token?parameters"
        payload = {
            "grant_type": "client_credentials",
            "client_id": settings.CDEK_CLIENT_ID,
            "client_secret": settings.CDEK_CLIENT_SECRET
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            self.cdek_auth_token = f"Bearer {data.get('access_token')}"
            return f"Bearer {data.get('access_token')}"
        else:
            print(f"Failed to obtain access token. Status code: {response.status_code}, Response: {response.text}")
            return None
