import os
import requests
import json


# Класс для обращения к API MailCatcher
class MailCatcher:
    # Получаем все сообщения
    @staticmethod
    def get_messages():
        return MailCatcher.get_response("messages", "get")

    @staticmethod
    # Очищаем всю почту
    def delete_messages():
        MailCatcher.get_response("messages", "delete")

    @staticmethod
    def get_response(host, method):
        base_url = f"http://controller.{os.environ['CLUSTER_TEST']}.notkube.dev.ivi.ru:1080/"

        url = base_url + host

        return requests.request(method, url).text

    @staticmethod
    def get_mail_catcher_html_internal(phone_number):
        id = MailCatcher.get_id_by_phone_number(phone_number)
        return MailCatcher.get_html_by_id(id)

    @staticmethod
    # Получаем нужный код из сообщения
    def get_id_by_phone_number(phone_number):
        message = MailCatcher.get_messages()
        message_object = json.loads(message)

        for message in message_object:
            if MailCatcher.filter_by_recipients(message['recipients'], phone_number):
                print(message['id'])
                return message['id']

    @staticmethod
    # получаем код из письма по урлу вида /messages/<id письма>.html
    def get_html_by_id(id):
        return MailCatcher.get_response("messages/" + str(id) + ".html", "get")

    @staticmethod
    # фильтруем список адресатов по нужному номеру телефона
    def filter_by_recipients(recipients, phone_number):
        for recipient in recipients:
            if recipient.find(phone_number) > -1:
                return True
