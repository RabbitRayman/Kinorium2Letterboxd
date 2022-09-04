# Kinorium2Letterboxd
Конвертер для CSV-файла от [Кинориума](https://ru.kinorium.com/) в формат, позволяющий импортировать оценки в [Letterboxd](https://letterboxd.com/)

Ссылка для скачивания exe-файла - https://disk.yandex.ru/d/nvf1GYngWWMVVQ.

Конвертация из .py в .exe произведена при помощи [Auto PY to EXE](https://pypi.org/project/auto-py-to-exe/).

## Инструкция по использованию:

### (опционально) Импорт оценок из Кинопоиска в Кинориум

В случае, если вы хотите импортировать в Letterboxd оценки из своего аккаунта на Кинопоиске, в первую очередь вам требуется произвести импорт оценок из Кинопоиска в Кинориум. Это выполняется непосредственно на сайте Кинориума, в разделе "Настройки".

![image](https://user-images.githubusercontent.com/22303711/188305487-540fae36-05d3-4512-a9b4-76cfdc129cbd.png)

![image](https://user-images.githubusercontent.com/22303711/188305503-e8542aaa-ef32-45bd-9cfb-f047740abf26.png)

### 1. Экспорт оценок из Кинориума

На сайте Кинориума, в разделе "Настройки", откройте вкладку "Резервное копирование". Там оставьте активным только переключатель "Оценки и просмотры" (как на изображении ниже), после чего нажмите кнопку "Отправить файл на почту". После получения данного файла, скачайте его на свой компьютер.

![image](https://user-images.githubusercontent.com/22303711/188305682-0bb918cc-e9eb-44c3-8830-7282cd2a7e49.png)

### 2. Формирование нового CSV-файла

Далее, запустите скачанный ранее файл GUI.exe. Откроется окно, в котором сначала при помощи кнопки "Выбрать файл" необходимо найти и выбрать присланный на почти и скачанный на ПК CSV-файл от Кинориума. После того как в поле рядом с кнопкой "Выбрать файл" будет отображен адрес, по которому находится данный файл (пример на изображении ниже), нажмите на кнопку "Сформировать CSV-файл для Letterboxd", после чего высветится сообщение об успехе, а в папке с GUI.exe появится файл letterboxd.csv

**Важно!** Есть вероятность того, что после нажатия кнопки "Сформировать CSV-файл для Letterboxd", антивирус (в частности, такое случается при использовании Avast) откроет окно с сообщением по типу "GUI.exe пытается изменить или удалить файл LETTERBOXD.CSV в защищенной папке". Однако, файл letterboxd.csv ещё даже не создан, а антивирус как раз-таки блокирует его создание.

![image](https://user-images.githubusercontent.com/22303711/188308236-e14d51b6-d4f3-4850-8771-534a6d357c02.png)

![image](https://user-images.githubusercontent.com/22303711/188308409-62fb5187-ccd8-4411-af84-18455abaaa94.png)

### 3. Импорт оценок в Letterboxd

Далее, на сайте Letterboxd зайдите в раздел "Settings" и там откройте вкладку "Import & Export". На данной вкладке нажмите на кнопку "Import your data", после чего откроется новая страница. Там нажмите на кнопку "Select A File" и в открывшемся окне найдите созданный в прошлом пункте файл letterboxd.csv, после чего дождитесь переноса оценок.

![image](https://user-images.githubusercontent.com/22303711/188308471-03935c5b-f79f-443f-b0ad-80b7b4c474c5.png)

![image](https://user-images.githubusercontent.com/22303711/188308540-02dbe193-6b46-4e3a-9c98-556d58bd8877.png)

**Важно!** В редких случаях, встречается ситуация, когда Letterboxd неверно идентифицирует фильм и оценка/метка о просмотре выставляются не той картине. В частности, такое случается с лентами "Дылда" (2019) Кантемира Балагова, "Охота" (2020) Крейга Зобела, "Одержимость" (2014) Дэмьена Шазелла, "Призрак в доспехах" (1995) Мамору Осии. Ошибки единичные (в частности, на 1200+ фильмов встречено всего четыре таких неточности), но всё равно неприятные, поэтому после импорта оценок перепроверьте какие фильмы были добавлены в ваш аккаунт Letterboxd.
