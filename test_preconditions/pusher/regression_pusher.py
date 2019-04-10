from test_preconditions.pusher.pull import DeliveryPull, send_pull, send_set_pull

from test_preconditions.pusher.config import *


class RegressionPull:
    """
    класс объединяет все функции отправки pull-уведомлений с предустановленными параметрами,
    но лучше использовать send_pull() - универсальную функцию отправки pull-уведомлений
    """
    @staticmethod
    def pull_small_text(ids=USER_ID,
                        feature_id=FEATURE_ID_CONTENT,
                        template=PULL_TEMPLATE_DEFAULT_CONTENT,
                        obj_id=CONTENT_ID,
                        obj_type=CONTENT,
                        url=PUSHER_DELIVERY_URL,
                        text="Тест пулла с коротким текстом"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text)

    @staticmethod
    def pull_no_text(ids=USER_ID,
                     feature_id=FEATURE_ID_CONTENT,
                     template=PULL_TEMPLATE_DEFAULT_CONTENT,
                     obj_id=CONTENT_ID2,
                     obj_type=CONTENT,
                     url=PUSHER_DELIVERY_URL,
                     text=""):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text)

    @staticmethod
    def pull_long_text(ids=USER_ID,
                       feature_id=FEATURE_ID_CONTENT,
                       template=PULL_TEMPLATE_DEFAULT_CONTENT,
                       obj_id=CONTENT_ID3,
                       obj_type=CONTENT,
                       url=PUSHER_DELIVERY_URL,
                       text="Все счастливые семьи похожи друг на друга, каждая "
                            "несчастливая семья несчастлива по-своему. "
                            "Все смешалось в доме Облонских. Жена узнала, "
                            "что муж был в связи с бывшею в их доме "
                            "француженкою-гувернанткой, и объявила мужу, "
                            "что не может жить с ним в одном доме. "
                            "Положение это продолжалось уже третий день и мучительно "
                            "чувствовалось и самими супругами, и всеми членами семьи, "
                            "и домочадцами."):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text)

    @staticmethod
    def pull_overly_long_text(ids=USER_ID,
                              feature_id=FEATURE_ID_CONTENT,
                              template=PULL_TEMPLATE_DEFAULT_CONTENT,
                              obj_id=CONTENT_ID3,
                              obj_type=CONTENT,
                              url=PUSHER_DELIVERY_URL,
                              text="Бал только что начался, когда Кити с матерью входила на большую, "
                                   "уставленную цветами и лакеями в пудре и красных кафтанах, залитую светом лестницу. "
                                   "Из зал несся стоявший в них равномерный, как в улье, шорох движенья, и, "
                                   "пока они на площадке между деревьями оправляли перед зеркалом прически и платья, "
                                   "из залы послышались осторожно-отчетливые звуки скрипок оркестра, "
                                   "начавшего первый вальс. "
                                   "Штатский старичок, оправлявший свои седые височки у другого зеркала и изливавший "
                                   "от себя запах духов, столкнулся с ними на лестнице и посторонился, видимо любуясь "
                                   "незнакомою ему Кити. Безбородый юноша, один из тех светских юношей, "
                                   "которых старый князь "
                                   "Щербацкий называл тютьками, в чрезвычайно открытом жилете, оправляя на ходу "
                                   "белый галстук, поклонился им и, пробежав мимо, вернулся, "
                                   "приглашая Кити на кадриль. "
                                   "Первая кадриль была уж отдана Вронскому, она должна "
                                   "была отдать этому юноше вторую. "
                                   "Военный, застегивая перчатку, сторонился у двери и, поглаживая усы, "
                                   "любовался на розовую Кити."
                                   "Несмотря на то, что туалет, прическа и все приготовления к балу "
                                   "стоили Кити больших "
                                   "трудов и соображений, она теперь, в своем сложном тюлевом платье на розовом чехле, "
                                   "вступала на бал так свободно и просто, как будто все эти розетки, кружева, "
                                   "все подробности туалета не стоили ей и ее домашним ни минуты внимания, как будто "
                                   "она родилась в этом тюле, кружевах, с этою высокою прической, "
                                   "с розой и двумя листками наверху ее."):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text)

    @staticmethod
    def pull_compilation(ids=USER_ID,
                         feature_id=FEATURE_ID_COMPILATION,
                         template=PULL_TEMPLATE_DEFAULT_COMPILATION,
                         obj_id=COMPILATION_ID,
                         obj_type=COMPILATION,
                         url=PUSHER_DELIVERY_URL):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type)

    @staticmethod
    def pull_user_action(ids=USER_ID,
                         feature_id=FEATURE_ID_TEXT,
                         template=PULL_TEMPLATE_DEFAULT_ACTION,
                         url=PUSHER_DELIVERY_URL,
                         action="/user/profile"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         action_for_pull=action,
                         certificate="test_cert")

    @staticmethod
    def pull_user_action_purchase_options(ids=USER_ID,
                                          feature_id=FEATURE_ID_ERROR,
                                          template=PULL_TEMPLATE_DEFAULT_ERROR,
                                          url=PUSHER_DELIVERY_URL):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url)

    @staticmethod
    def pull_cert_autocomplete(ids=USER_ID,
                               feature_id=FEATURE_ID_LAST_CHANCE,
                               template=PULL_TEMPLATE_DEFAULT_LAST_CHANCE,
                               url=PUSHER_DELIVERY_URL):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         certificate="cookies1")

    @staticmethod
    def pull_cert_auto_true(ids=USER_ID,
                            feature_id=FEATURE_ID_LAST_CHANCE,
                            template=PULL_TEMPLATE_DEFAULT_LAST_CHANCE,
                            url=PUSHER_DELIVERY_URL,
                            auto=1,
                            certificate="cookies2"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         certificate=certificate,
                         auto=auto)

    @staticmethod
    def pull_movie_open(ids=USER_ID,
                        feature_id=FEATURE_ID_CONTENT,
                        template=PULL_TEMPLATE_DEFAULT_CONTENT,
                        url=PUSHER_DELIVERY_URL,
                        obj_id=CONTENT_ID4,
                        obj_type=CONTENT,
                        text="Тестовый пулл с переходом на фильм"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text)

    @staticmethod
    def pull_movie_open_play(ids=USER_ID,
                             feature_id=FEATURE_ID_CONTENT,
                             template=PULL_TEMPLATE_DEFAULT_CONTENT,
                             url=PUSHER_DELIVERY_URL,
                             obj_id=CONTENT_ID2,
                             obj_type=CONTENT,
                             play=True,
                             text="Тестовый пулл с переходом на фильм c воспроизведением"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text,
                         play=play)

    @staticmethod
    def pull_movie_trailer(ids=USER_ID,
                           feature_id=FEATURE_ID_CONTENT,
                           template=PULL_TEMPLATE_DEFAULT_CONTENT,
                           url=PUSHER_DELIVERY_URL,
                           obj_id=CONTENT_ID,
                           obj_type=CONTENT,
                           trailer=True,
                           text="Тестовый пулл с переходом на трейлер"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text,
                         trailer=trailer)

    @staticmethod
    def pull_compilation_open(ids=USER_ID,
                              feature_id=FEATURE_ID_COMPILATION,
                              template=PULL_TEMPLATE_DEFAULT_COMPILATION,
                              url=PUSHER_DELIVERY_URL,
                              obj_id=COMPILATION_ID2,
                              obj_type=COMPILATION,
                              text="Пулл, который открывает карточку  Доктора Хауса"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         text=text)

    @staticmethod
    def pull_compilation_season(ids=USER_ID,
                                feature_id=FEATURE_ID_SEASON,
                                template=PULL_TEMPLATE_DEFAULT_SEASON,
                                url=PUSHER_DELIVERY_URL,
                                obj_id=COMPILATION_ID2,
                                obj_type=COMPILATION,
                                season=SEASON_NUM,
                                season_id=SEASON_ID,
                                text="Пулл, который открывает сезон  Доктора Хауса"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         season=season,
                         season_id=season_id,
                         text=text)

    @staticmethod
    def pull_collection_open(ids=USER_ID,
                             feature_id=FEATURE_ID_COLLECTION,
                             template=PULL_TEMPLATE_DEFAULT_COLLECTION,
                             url=PUSHER_DELIVERY_URL,
                             obj_id=COLLECTION_ID,
                             obj_type=COLLECTION,
                             play=False,
                             text="Тест  пулла коллекции (подборки)"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         play=play,
                         text=text)

    @staticmethod
    def pull_collection_open_play(ids=USER_ID,
                                  feature_id=FEATURE_ID_COLLECTION,
                                  template=PULL_TEMPLATE_DEFAULT_COLLECTION,
                                  url=PUSHER_DELIVERY_URL,
                                  obj_id=COLLECTION_ID,
                                  obj_type=COLLECTION,
                                  play=True,  # почему "play" ничего не решает?
                                  text="Тест  пулла коллекции (подборки) c play=True"):
        return send_pull({"feature_id": feature_id,
                          "messages": DeliveryPull.get_messages_pull(template),
                          "rule_params": {"user_ids": ids}},
                         url,
                         obj_id=obj_id,
                         obj_type=obj_type,
                         play=play,
                         text=text)


"""
После реализации добавления шаблона для каждого теста сделать адеватные методы:
1.Tестовый пулл с добавлением фильма в избранное с "action_for_pull": "/movie/favourite"
2.Tестовый пулл с добавлением сериала в избранное "action_for_pull": "/compilation/favourite"
3.Tестовый пулл, открывающий сортированную коллекцию с "action_for_pull": "/catalogue/open/",
                                                       "sort_by": sort_by
"""
