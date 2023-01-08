# REST-API-Automation-Testing

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Данный репозиторий содержит проект из курса "Автоматизация тестирования REST API на Python".

- Ссылка на курс: https://software-testing.ru/edu/3-online/321-rest-api-python
- API: https://playground.learnqa.ru/api/

> Полное описание заданий находится в файле ***full task description.***

## Описание задач:

### API requests

**Ex 1: Парсинг JSON**

С помощью библиотеки “json” распарсить переменную json_text и вывести текст второго сообщения с помощью функции print.

**Ex 2: Длинный редирект**

Необходимо написать скрипт, который создает GET-запрос на метод.
С помощью конструкции response.history необходимо узнать: 
1. Cколько редиректов происходит от изначальной точки назначения до итоговой? 
2. Какой URL итоговый?

**Ex 3: Запросы и методы**

Для URL (который принимает HTTP-методы: POST, GET, PUT, DELETE) написать скрипт, который делает следующее:
1. Отправляет http-запрос любого типа без параметра method;
2. Отправляет http-запрос не из списка. Например, HEAD;
3. Отправляет запрос с правильным значением method;
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.

**Ex 4: Токены**

GET-метод */longtime_job* без параметра token заводит новую задачу, а в ответ выдает нам JSON с полями:
* seconds - количество секунд, через сколько задача будет выполнена
* token - токен, по которому можно получить результат выполнения нашей задачи

GET-метод с параметром token, в ответ возвращает JSON:
* error - "No job linked to this token" в случае, если передать token, для которого не создавалась задача.
* status - "Job is NOT ready" если задача еще не готова, "Job is ready" - если же готова 
* result - будет только в случае, если задача готова, это поле будет содержать результат

Наша задача - написать скрипт, который будет делать следующее:
1. создавать задачу
2. отправлять запрос с token ДО того, как задача готова, убеждался в правильности поля status
3. ожидать нужное количество секунд с помощью функции time.sleep()
4. отправляь запрос c token ПОСЛЕ того, как задача готова, и убедиться в правильности поля status и наличии поля result

**Ex 5: Подбор пароля**

Необходимо подобрать пароль. Логин извествен, пароль один из 25 наиболее распространных паролей. 

POST-методом */get_secret_password_homework* с двумя с двумя параметрами: login и password, возвращаем  cookie с названием auth_cookie и каким-то значением.

Если login указан и существует, метод вернет нам авторизационную cookie с названием auth_cookie и каким-то значением.
Если верно указано поле login, но передан неправильный password, то авторизационная cookie все равно вернется, *но с "неправильным" значением*. Если и login, и password указаны верно, вернется cookie с "правильным" значением. Таким образом используя только метод get_secret_password_homework невозможно узнать, передали ли мы верный пароль или нет.

С помощью второго метода */check_auth_cookie*, проверяющего правильность нашей авторизованной cookie, проверяем авторизацию. 

Задача:
1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод. В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.
2. Далее эту cookie передается во второй метод. Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный. В этом случае берем следующий пароль и все заново. Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.

### Pytest


**Ex 6: Тест на короткую фразу**

C помощью pytest необходимо написать тест, который проверяет, что введенная в консоли фраза короче 15 символов.


**Ex 7: Тест запроса на метод cookie**

Необходимо написать тест, который делает запрос на метод */homework_cookie*

Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert


**Ex 8: Тест запроса на метод header**

Необходимо написать тест, который делает запрос на метод */homework_header*.

Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert


**Ex 9: User Agent**

Метод */user_agent_check* определяет по строке заголовка User Agent следующие параметры:

>device - iOS или Android
>
>browser - Chrome, Firefox или другой браузер
>
>platform - мобильное приложение или веб
>
>Если метод не может определить какой-то из параметров, он выставляет значение Unknown.

Наша задача написать параметризированный тест. Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения, GET-делать запрос с этим User Agent и убедиться, что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.

___________________________________________________

*В процессе выполнения:*

**Ex 10: Формирование фреймворка**

На этом уроке мы начали создавать свой фреймворк. 
Он нам пригодится в дальнейшим, так как домашние задания следующего урока будут опираться на методы из этого фреймворка.

Потом эта задача в том, чтобы повторить то, что мы проделали на уроке:

1. создать класс BaseCase в директории lib/

2. создать класс Assertions в директории lib/

3. создать тест TestUserAuth в директории tests/ 

**Ex 11: Тесты на метод user**

В соответствующем классе TestUserRegister необходимо написать больше тестов на создающий пользователя POST-метод: api/user/

Список тестов:

- Создание пользователя с некорректным email - без символа @

- Создание пользователя без указания одного из полей 
с помощью @parametrize необходимо проверить, что отсутствие любого параметра не дает зарегистрировать пользователя

- Создание пользователя с очень коротким именем в один символ

- Создание пользователя с очень длинным именем - длиннее 250 символов

**Ex 12: Запрос данных другого пользователя**

На занятиях в классе TestUserGet мы писали тест на запрос, показывающий данные пользователя. Мы покрыли тестами два кейса:

неавторизованный запрос на данные - там мы получили только username

авторизованный запрос - мы были авторизованы пользователем с ID 2 и делали запрос для получения данных того же пользователя, в этом случае мы получали все поля

В этой задаче нужно написать тест, который авторизовывается одним пользователем, но получает данные другого (т.е. с другим ID). И убедиться, что в этом случае запрос также получает только username, так как мы не должны видеть остальные данные чужого пользователя.

**Ex 13: Негативные тесты на PUT**

Написать негативные тесты для PUT-метода:

Необходимо:
- изменить данные пользователя, будучи неавторизованными; 
- изменить данные пользователя, будучи авторизованными другим пользователем;
- изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @ 
- изменить firstName пользователя, будучи авторизованными тем же пользователем, на короткое значение в один символ

**Ex 14: Тесты на DELETE**

У нас есть метод, который удаляет пользователя по ID - DELETE-метод api/user/{id}. 

Удалить можно только того пользователя, из-под которого вы авторизованы. Необходимо в директории tests/ создать новый файл test_user_delete.py с классом TestUserDelete.

Там написать следующие тесты:

1. Попытка удалить пользователя по ID 
  Его данные для авторизации:

>data = {
>
>   'email': 'vinkotov@example.com',
>
>    'password': '1234'
>
>}

Убедиться, что система не даст вам удалить этого пользователя.

2. Позитивный. Создать пользователя, авторизоваться из-под него, удалить, затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.

3. Негативный. попробовать удалить пользователя, будучи авторизованными другим пользователем.

**Ex14: Теги Allure**

Давайте добавим больше Allure-тегов во все написанные нами тесты. Выбирайте любые, которые понравятся из официальной документации - https://docs.qameta.io/allure/

Цель задания - поэкспериментировать с бОльшим количеством тегов, узнать, где именно в отчете они отображаются. В этом задании не будет правильных и неправильных результатов. Но все же нам очень интересно посмотреть, какие теги вы сочтете особенно полезными для вашего фреймворка.
