import allure
import requests

"""List HTTP methods"""

headers = {'Content-Type': 'application/json'}
cookie = ""


def method_get(url, params):
    with allure.step("GET"):
        if params is None:
            params = ""
        result = requests.get(url, params=params, headers=headers, cookies=cookie, verify=True)
        return result


def method_post(url, body):
    with allure.step('POST'):
        result = requests.post(url, json=body, headers=headers, cookies=cookie,
                               verify=False)
        return result


def method_put(url, body):
    with allure.step("PUT"):
        result = requests.put(url, json=body, headers=headers, cookies=cookie,
                              verify=False)
        return result


def method_delete(url, body):
    with allure.step("DELETE"):
        result = requests.delete(url, json=body, headers=headers, cookies=cookie,
                                 verify=False)
        return result

# w