# Библиотека для работы с тестовыми предусловиями

### Что это?

Библиотека тестовых предусловий предоставляет высокоуровневый доступ к API бэкенда.
Теперь нет необходимости штудировать многочисленные доки сервисов, изучать схемы баз данных,
все необходимые методы для клиентского тестирования должна предоставлять данная 
библиотека. 

Пример использования:

```python
>>> from test_preconditions.content_list_generation.generate import content_by_type

>>> content_by_type(['TVOD'], 2, 'single', adult=False)

[{'content_id': 105825, 'title': 'Роман с камнем'}, {'content_id': 115550, 'title': 'Прогулка в облаках'}]
```

### Как установить?

Проект хранится в разделе http://gitlab.dev.ivi.ru/qa_automation/test_preconditions

Оттуда библиотека устанавливается в ваш проект с помощью **pip**.

```bash
pip install git+http://gitlab.dev.ivi.ru/qa_automation/test_preconditions
```

Библиотека использует переменную окружения CLUSTER_TEST. Передавать так:

```bash
$ export CLUSTER_TEST=sscluster
```

Проверить, что храниться в переменной:

```bash
$ echo $CLUSTER_TEST
sscluster
```

### Что умеет?

- Генерировать списки контента по заданным признакам:

```python
>>> from test_preconditions.content_list_generation.generate import content_by_type

>>> content_by_type(['TVOD'], 2, 'single', adult=True)

[{'content_id': 105825, 'title': 'Роман с камнем'}, {'content_id': 115550, 'title': 'Прогулка в облаках'}]

```

```python
>>> from test_preconditions.content_list_generation.generate import compilation_by_type

>>> compilation_by_type('with_seasons', ['EST'], 2, adult=True)

[{'compilation_id': 7893, 'title': 'Шерлок'}, {'compilation_id': 8002, 'title': 'Родина'}]

```

- Генерировать списки предзаказа:

```python
>>> from test_preconditions.content_list_generation.generate import preorder

>>> preorder(count=3)

[{'id': 133371, 'title': 'Гринч'}, {'id': 133589, 'title': 'Капитан Марвел'}, {'id': 131247, 'title': 'Как приручить дракона 3'}]

```

- Создавать пользователей

```python
>>> from test_preconditions.user_creation.register import register_email

>>> register_email()

[{'app_version': '870',
  'email': 'testxxlvp8gi8p_0@ivi.ru',
  'password': '111111',
  'session': 'acc8e49333_1558614115-33Y0qSZZrsOSXfijbbSvBDeQ',
  'uid': '33'}]
```

- Генерировать сертификаты

```python
>>> from test_preconditions.certificate import certificate

>>> keys = certificate.create()
    Пример:
        cert = certificate.create(type='content', id=171864)
    # Возвращает список ключей сертификатов (по умолчанию 1 сертификат на подписку без привязки карты)
    Принимает параметры:
    :param type: На что сертификат - 'subscription' (по умолчанию), 'content', 'compilation'
    :param card: Требуется ли привязка карты. 't' - да, 'f' - нет (по умолчанию).
    :param id: id контента. Для подписки 6 (по умолчанию).
    :param quality: Качество контента. 'HD' (по умолчанию)
    :param count: Количество сертификатов. 1 (по умолчанию)
```

- Совершать покупки через API сервиса Profit

```python
>>> from test_preconditions.purchase.user_purchases import content_purchase

>>> content_purchase([1,2,3], [64239], 'content', 'eternal')

[{'content_id': 64239,
  'content_type': 'content',
  'ownership': 'eternal',
  'quality': 'HD',
  'uid': 1},
 {'content_id': 64239,
  'content_type': 'content',
  'ownership': 'eternal',
  'quality': 'HD',
  'uid': 2},
 {'content_id': 64239,
  'content_type': 'content',
  'ownership': 'eternal',
  'quality': 'HD',
  'uid': 3}]
```

```python
>>> from test_preconditions.purchase.user_purchases import subscription_purchase

>>> subscription_purchase([1])

[{'content_id': 6,
  'content_type': 'subscription',
  'ownership': 'temporal',
  'quality': 'HD',
  'uid': 1}]
```

- Создавать pull-уведомления

```python
>>> from test_preconditions.pusher.pull import delivery_create

>>> delivery_create(uid=1)
```

- Получать/очищать код из смс уведомлений

```python
>>> from test_preconditions.mailcatcher.mailcatcher import MailCatcher

Получаем код по номеру телефона:
>>> MailCatcher.get_mail_catcher_html_internal("79112223344")

Очищаем полностью mailcatcher на некубе:
>>> MailCatcher.delete_messages()

```

- Получить uid пользователя по номеру телефона или email

```python
>>> from test_preconditions.user_creation import uid

>>> uig.get_uid("79167719078")

3022
```

- Отменить подписку пользователя

```python
>>> from test_preconditions.purchase.user_purchases import cancel_subscription

>>> cancel_subscription(2722)
```
