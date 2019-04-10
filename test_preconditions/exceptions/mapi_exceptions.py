class MapiError(Exception):
    """Мапи ответило с ошибкой в теле ответа.
    Выбросить эту ошибку, указав в message метод,
    в котором произошла ошибка, и сообщение из ответа мапи.

    message=f"register_user_by_email(): got error from mapi: {response_body['error']}"

    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
