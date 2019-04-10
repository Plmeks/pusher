import requests
import time
import random
import string


class ParamsDelivery:
    def __init__(self):
        """
        конструктор, инициализирует дефолтные параметры и список параметров, с которыми сожно работать
        list_possible_params: список возможных параметров, их типов, информация об их обязательности
        params: дефолтные параметры рассылки, не все обязательные параметры заполнены
        """
        self.list_possibles_parameters = [{"name": "b2b_id", "type": str, "required": True},
                                          {"name": "app_versions", "type": list, "required": False},
                                          {"name": "messages", "type": list, "required": True},
                                          {"name": "rule", "type": int, "required": False},
                                          {"name": "params", "type": dict, "required": False},
                                          {"name": "start_datetime", "type": int, "required": True},
                                          {"name": "stop_datetime", "type": int, "required": True},
                                          {"name": "begin_daylight", "type": int, "required": False},
                                          {"name": "end_daylight", "type": int, "required": False},
                                          {"name": "timeout", "type": int, "required": False},
                                          {"name": "priority", "type": int, "required": False},
                                          {"name": "consider_local_time", "type": bool, "required": False},
                                          {"name": "consider_email_confirmed", "type": bool, "required": False},
                                          {"name": "uniq", "type": bool, "required": False},
                                          {"name": "paid_types", "type": list, "required": False},
                                          {"name": "delete_after_stop_time", "type": bool, "required": False},
                                          {"name": "dont_send_sms_if_email", "type": bool, "required": False},
                                          {"name": "dry_run", "type": bool, "required": False},
                                          {"name": "title", "type": str, "required": False},
                                          {"name": "rule_params", "type": dict, "required": False},
                                          {"name": "feature_id", "type": int, "required": True},
                                          {"name": "status", "type": int, "required": True}]

        current_time = int(time.time())

        self.parameters = {"b2b_id": self.generate_b2b_id(),
                           "app_versions": [],
                           "rule": 3,  # по умолчанию отправляем на заданный список пользователей, если 1, то на всех
                           "params": {},
                           "start_datetime": current_time,  # текущее время округлённое в меньшую сторону
                           "stop_datetime": current_time + 86400,  # + день по
                           "status": 3,  # по умолчанию статус рассылки: "подтверждена"
                           "priority": 5,  # 0..10, чем выше приоритет, тем выше в очереди
                           "consider_local_time": False,
                           "consider_email_confirmed": False,
                           "dry_run": False,
                           "title": "Регресс",
                           "rule_params": {"user_ids": []}}

    @staticmethod
    def generate_b2b_id():
        """
        статический метод генерации уникальных b2b_id
        :return: строка, которую можно использовать, как b2b_id
        """
        random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        b2b_id = f'auto_create_{int(time.time())}{random_string}'
        return b2b_id

    def get_names_parameters(self):
        """
        метод получения списка допустимых параметров в запросе
        :return: список, содержащий наименования возможных параметров
        """
        params_names = []
        for param in self.list_possibles_parameters:
            params_names.append(param["name"])
        return params_names

    def get_required_parameters(self):

        """
        метод получения списка обязательных параметров в запросе
        :return: список, содержащий наименования обязательных параметров
        """
        params_names = []
        for param in self.list_possibles_parameters:
            if param["required"] is True:
                params_names.append(param["name"])
        return params_names

    def change_parameters(self, new_param):
        """
        полностью меняет параметры keys на переданное значение в словаре
        игнорирует параметры, которые нельзя передать в запросе (не возвращаются в get_names_params())
        :param new_param: словарь, где ключ - название параметра для замены, значение - на что заменить

        пример: pull.change_params({"name": "test", "params": {
            "obj_id": id,
            "obj_type": 1,
            "resume_time": resume_time
        }})

        данный вызов проигнорирует параметр name и изменит значение параметра params
        на словарь {"obj_id": id,
                    "obj_type": 1,
                    "resume_time": resume_time}
        """
        for key in new_param:
            if key in self.get_names_parameters():
                self.parameters.update({key: new_param[key]})

    def change_params(self, **kwargs):
        self.parameters["params"].update(kwargs)

    def set_params(self, **kwargs):
        self.parameters["params"] = {}
        self.parameters["params"].update(kwargs)

    def set_parameters(self, new_params):
        """
        очищает все параметры по умолчанию и задаёт пользовательские
        игнорирует параметры, которые нельзя передать в запросе (не возвращаются в get_names_params())
        использовать с осторожностью
        :param new_params: пользовательские параметры
        """
        self.parameters = {}
        self.change_parameters(new_params)

    def check_required_parameters(self):
        """
        проверяет сам факт наличия всех обязательных параметров в params
        :return: bool, True, если все обязательные параметры заполнены,
                       иначе False
        """
        count_params = 0
        list_required_params = self.get_required_parameters()
        for param_name in self.parameters:
            if param_name in list_required_params:
                count_params += 1
        if count_params != len(list_required_params):
            return False
        return True

    def check_types_parameters(self):
        """
        проверяет соответствие типов в self.params и ожидаемых сервером
        :return: bool, True, если все типы заданы верно,
                       иначе False
        """
        for param in self.list_possibles_parameters:
            if param["name"] in self.parameters.keys():
                if type(self.parameters[param["name"]]) is not param["type"]:
                    return False
        return True


class Delivery(ParamsDelivery):
    def __init__(self):
        """
        конструктор, инициализирует параметры по умолчанию и список с информацией о возможных параметрах
        headers: используемые заголовки
        delivery_status: status рассылки, по умолчанию None, в случае отправки запроса на сервер - ответ сервера,
                                                             в случае неуспешного заполнения параметров - False
        """
        super().__init__()
        self.headers = {}
        self.delivery_status = None

    def check_delivery(self):
        """
        проверяет готовность объекта Delivery  к отправке
        :return: bool, True - если все проверки пройдены,
                       иначе False
        """
        if self.check_types_parameters() and \
                self.check_required_parameters():
            return True
        return False

    def send_delivery(self, url):
        """
        отправляет Delivery запросом на url
        :param url: строка, адрес, куда совершать отправку
        :return: ответ сервера
        """
        if not self.check_delivery():
            self.delivery_status = False
            return False
        req = requests.Session()
        req.headers.update(self.headers)
        response = req.post(url, json=self.parameters)
        self.delivery_status = response.status_code
        return response

    def check_delivery_status(self, status=201):
        if self.delivery_status != status:
            if not self.delivery_status:
                print(f"Рассылка не отправлена, так как не прошла проверки")
            else:
                print(f"Рассылка отправлена неуспешно, сервер вернул {self.delivery_status}")
            return False
        return True
