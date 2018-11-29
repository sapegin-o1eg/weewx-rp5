weewx-rp5 - выгрузка данных на сайт rp5.ru. Далее Модуль.


Описание:
  Модуль позволяет автоматически выгружать архивные данные на сайт rp5.ru, используя API (https://rp5.ru/docs/sgate/ru)

Требования:
  Для передачи данных, необходимо предварительно получить api_key (Инструкция по получению тут
  https://rp5.ru/docs/sgate/ru, пункт "Регистрация")

Инструкция по установке:
  Существует два метода установки модуля
    - ручной
    - автоматический, используя утилиту wee_extension (http://weewx.com/docs/utilities.htm#wee_extension_utility)

    Допустим, что:
      "/home/weewx/bin" директория bin установленной версии WeeWX
      "/tmp" директория для скачивания установочного файла

Автоматическая установка с помощью wee_extension:
  1. Загрузите последнюю версию Модуля https://github.com/sapegin-o1eg/weewx-rp5/releases
      wget -P /tmp https://github.com/sapegin-o1eg/weewx-rp5/releases/download/v0.2/weewx-rp5-0.2.tar.gz

  2. Остановите WeeWX
      sudo /etc/init.d/weewx stop
      или
      sudo service weewx stop

  3. Установите модуль используя утилиту wee_extension
      cd /home/weewx/bin
      ./wee_extension --install=/tmp/weewx-rp5-0.2.tar.gz

  4. Отредактируйте конфигурационный файл weewx.conf
      vim /home/weewx/weewx.conf

  5. В файле weewx.conf под секциями [StdRESTful] [[RP5]] убедитесь, что значению enable присвоено значение true,
      а значению api_key присвоен Ваш api_key, полученный при регистрации (см. пункт "Требования")

        [[RP5]]
          enable = true
          api_key = Ваш_API_KEY

  6. Сохраните файл weewx.conf.

  7. Запустите WeeWX:
      sudo /etc/init.d/weewx start
      или
      sudo service weewx start

  8. В случае возникновения проблем с выгрузкой данных, следует указать в файле weewx.conf значение debug=2. Как
       следствие, в лог файле syslogd будет содержаться отладочная информация, которая, в свою очередь, будет полезна
       для выявления причин.

Ручная установка:
  1. Загрузите последнюю версию Модуля https://github.com/sapegin-o1eg/weewx-rp5/releases
      wget -P /tmp https://github.com/sapegin-o1eg/weewx-rp5/releases/download/v0.2/weewx-rp5-0.2.tar.gz

  2. Остановите WeeWX
      sudo /etc/init.d/weewx stop
      или
      sudo service weewx stop

  3. Распакуйте установочный файл
      tar xvfz weewx-rp5-0.2.tar.gz

  4. Скопируйте распакованные файлы
      cp weewx-rp/bin/user/*.py /home/weewx/bin/user

  5. Отредактируйте конфигурационный файл weewx.conf
      vim weewx.conf

  6. В файле weewx.conf, под секциями [StdRESTful] [[RP5]] убедитесь, что значению enable присвоено значение true,
      а значению api_key присвоен Ваш api_key, полученный при регистрации (см. пункт "Требования")

        [[RP5]]
          enable = true
          api_key = Ваш_API_KEY

  7. В файле weewx.conf, под секцией [Services] добавьте user.rp5.StdRP5 в список restful_services:

        [Services]
          ...
          restful_services = ..., user.rp5.StdRP5
          ...

  8. Сохраните файл weewx.conf.

  9. Запустите WeeWX:
      sudo /etc/init.d/weewx start
      или
      sudo service weewx start

  10. В случае возникновения проблем с выгрузкой данных, следует указать в файле weewx.conf значение debug=2. Как
       следствие, в лог файле syslogd будет содержаться отладочная информация, которая, в свою очередь, будет полезна
       для выявления причин.