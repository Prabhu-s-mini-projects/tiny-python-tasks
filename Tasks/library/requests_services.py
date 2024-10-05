""" Contains all the utils methods """
# Dependencies
import requests


# Custom exception for handling request errors-------------------
class RequestError(Exception):
    """Custom exception for request errors"""
    pass


# Decorator Methods ----------------------------------------------
def response_handler(func):
    """Acts as decorator"""

    def wrap_func(*args, **kwargs):
        """Wrapper function"""
        try:
            response = func(*args, **kwargs)
            print(f"URL: {response.url}")
            print(f"Status Code: {response.status_code}")
            print(f"{response.text = }")

            # Raise exception for bad status codes
            response.raise_for_status()

            # returns the entire response
            return response

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {str(e)}")
            raise RequestError(f"Request failed: {str(e)}") from e

    return wrap_func


# Class ----------------------------------------------------------

class RequestService:
    """Helper class to easily access request methods"""

    def __init__(self, default_headers: dict = None):
        """Initialize with optional default headers"""
        self.default_headers = default_headers if default_headers else {}

    def merge_headers(self, custom_headers: dict = None) -> dict:
        """Merge default headers with custom headers for a request"""
        if custom_headers:
            return {**self.default_headers, **custom_headers}
        return self.default_headers

    @response_handler
    def post(self, url: str, data_params: dict, headers: dict = None) -> requests.Response:
        """POST request with optional custom headers"""
        all_headers = self.merge_headers(headers)
        return requests.post(url=url, json=data_params, headers=all_headers, timeout=10)

    @response_handler
    def get(self, url: str, data_params: dict = None, headers: dict = None) -> requests.Response:
        """GET request with optional custom headers"""
        all_headers = self.merge_headers(headers)
        return requests.get(url=url, params=data_params, headers=all_headers, timeout=10)

    @response_handler
    def put(self, url: str, data_params: dict, headers: dict = None) -> requests.Response:
        """PUT request with optional custom headers"""
        all_headers = self.merge_headers(headers)
        return requests.put(url=url, json=data_params, headers=all_headers, timeout=10)

    @response_handler
    def delete(self, url: str, data_params: dict = None, headers: dict = None) -> requests.Response:
        """DELETE request with optional custom headers"""
        all_headers = self.merge_headers(headers)
        return requests.delete(url=url, json=data_params, headers=all_headers, timeout=10)
