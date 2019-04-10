import os

PUSHER_URL = f"http://pusher.{os.environ['CLUSTER_TEST']}.notkube.dev.ivi.ru"
PUSHER_DELIVERY_URL = f"{PUSHER_URL}/delivery"

PULL_CLASSIFICATION_ID = 54  # тип канала доставки == pull

CONTENT_ID = 142555  # фильм "Малыш на драйве"
CONTENT_ID2 = 7029  # улучшайзер
CONTENT_ID3 = 96097  # фильм "Анна Каренина"
CONTENT_ID4 = 190667  # фильм "Шпион, который меня кинул"

COMPILATION_ID = 10570  # сериал "Записки юного врача"
COMPILATION_ID2 = 9224  # сериал "Доктор Хаус"

COLLECTION_ID = 8266  # подборка фильмов вселенной DC
COLLECTION_ID2 = 3307  # подборка фильмов с неожиданной концовкой

CONTENT = 1  # тип объекта контент
COMPILATION = 2  # тип объекта сборник
COLLECTION = 4  # тип коллекция/подборка

SEASON_NUM = 2  # номер сезона не первый, существующий
SEASON_ID = 166  # id второго сезона сериала "Доктор Хаус"

FEATURE_ID_CONTENT = 2  # тип сообщения - контент, вид отписки - новинки
FEATURE_ID_COMPILATION = 22  # тип сообщения - возобновить просмотр, вид отписки - вы на ivi
FEATURE_ID_SEASON = 3  # тип сообщения - сборник, вид отписки - новинки
FEATURE_ID_TEXT = 6  # тип сообщения - текст, тип отписки - подарки и специальные предложения
FEATURE_ID_ERROR = 9  # тип сообщения - ошибка в автопродлении
FEATURE_ID_LAST_CHANCE = 20  # тип сообщения - последний шанс
FEATURE_ID_COLLECTION = 50  # тип сообщения - подраки

PULL_TEMPLATE_DEFAULT_CONTENT = 345  # контент с открытием
PULL_TEMPLATE_DEFAULT_SEASON = 370  # сезон с открытием
PULL_TEMPLATE_DEFAULT_ERROR = 11  # ошибка в автопродлении
PULL_TEMPLATE_DEFAULT_COMPILATION = 39  # сборник с открытием
PULL_TEMPLATE_DEFAULT_ACTION = 473  # шаблон, приветствующий Женю
PULL_TEMPLATE_DEFAULT_LAST_CHANCE = 12
PULL_TEMPLATE_DEFAULT_COLLECTION = 526

USER_ID = (2,)
