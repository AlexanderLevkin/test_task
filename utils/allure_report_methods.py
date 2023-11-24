import allure
import json


def attach_response_json(response, name):
    allure.attach(body=json.dumps(response, indent=4), name=name,
                  attachment_type=allure.attachment_type.JSON)


def attach_response_text(text, name):
    allure.attach(text, name=name,
                  attachment_type=allure.attachment_type.TEXT)


def attach_response_picture(screenshot, name):
    allure.attach(screenshot, name=name,
                  attachment_type=allure.attachment_type.PNG)
