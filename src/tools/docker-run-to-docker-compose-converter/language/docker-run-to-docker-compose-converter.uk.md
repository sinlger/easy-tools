# Документація до конвертера Docker Run в Docker-Compose

## 1. Огляд інструменту

Конвертер Docker Run в Docker-Compose — це зручний онлайн-інструмент, який допомагає розробникам перетворювати команди "docker run" у файли формату Docker-Compose. Це спрощує процес налаштування оркестрування контейнерів та підвищує ефективність розробки.

## 2. Основні функції

1. **Конвертація команд**
   * Користувачі можуть вставляти складні команди Docker, наприклад: "docker run -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock:ro --restart always --log-opt max-size=1g nginx", у спеціальне поле введення.
   * Інструмент автоматично аналізує всі параметри команди "docker run", зокрема мапінг портів ("-p 80:80"), монтування томів ("-v /var/run/docker.sock:/tmp/docker.sock:ro"), політики перезапуску ("--restart always"), опції журналу ("--log-opt max-size=1g") та назву образу ("nginx").

2. **Створення файлів Docker-Compose**
   * На основі проаналізованих параметрів команди "docker run" генерується відповідний вміст файлу Docker-Compose.
   * Згенерований YAML-файл містить оголошення версії (наприклад, "version: '3.9'"), визначення сервісів ("services"), вказівку образу ("image"), конфігурацію журналу ("logging" з "options"), налаштування перезапуску ("restart"), прив’язку томів ("volumes") та мапінг портів ("ports"). Таким чином, вся необхідна інформація для оркестрування контейнерів подається повною мірою, що дозволяє користувачам безпосередньо застосовувати файл або вносити додаткові зміни.

3. **Завантаження файлу**
   * Кнопка "Download docker-compose.yml" дає змогу користувачам одноразовим кліком завантажити створений файл Docker-Compose на локальний комп’ютер. Це значно спрощує його використання в реальних проектних середовищах.