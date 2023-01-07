## Подробное описание заданий

### API requests

**Ex 1: Парсинг JSON**

С помощью библиотеки “json” распарсить переменную json_text и вывести текст второго сообщения с помощью функции print.

```sh
{
  "messages": [
    {
      "message": "This is the first message",
      "timestamp": "2021-06-04 16:40:53"
    },
    {
      "message": "And this is a second message",
      "timestamp": "2021-06-04 16:41:01"
    }
  ]
}
```


**Ex 2: Длинный редирект**

Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect

С помощью конструкции response.history необходимо узнать: 
1. Cколько редиректов происходит от изначальной точки назначения до итоговой? 
2. Какой URL итоговый?


**Ex 3: Запросы и методы**

У нас есть следующий URL: https://playground.learnqa.ru/ajax/api/compare_query_type

Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE

При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос. 

Надо написать скрипт, который делает следующее:
1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.

Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.


**Ex 4: Токены**

Иногда API-метод выполняет такую долгую задачу, что за один HTTP-запрос от него нельзя сразу получить готовый ответ. Это может быть подсчет каких-то сложных вычислений или необходимость собрать информацию по разным источникам. В этом случае на первый запрос API начинает выполнения задачи, а на последующие либо говорит, что задача еще не готова,  либо выдает результат. 

API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job

Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:

> * seconds - количество секунд, через сколько задача будет выполнена
> * token - тот самый токен, по которому можно получить результат выполнения нашей задачи

Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:

> * error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе будет следующая надпись - No job linked to this token
> * status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
> * result - будет только в случае, если задача готова, это поле будет содержать результат

Наша задача - написать скрипт, который делал бы следующее:
1) создавал задачу
2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result


**Ex 5: Подбор пароля**

Сегодня к нам пришел наш коллега и сказал, что забыл свой пароль от важного сервиса. Он просит нас помочь ему написать программу, которая подберет его пароль.

Есть метод: https://playground.learnqa.ru/ajax/api/get_secret_password_homework
> Его необходимо вызывать POST-запросом с двумя параметрами: login и password.
>
> Если вызвать метод без поля login или указать несуществующий login, метод вернет 500.
>
> Если login указан и существует, метод вернет нам авторизационную cookie с названием auth_cookie и каким-то значением.

У метода существует защита от перебора. Если верно указано поле login, но передан неправильный password, то авторизационная cookie все равно вернется. НО с "неправильным" значением, которое на самом деле не позволит создавать авторизованные запросы. Только если и login, и password указаны верно, вернется cookie с "правильным" значением. Таким образом используя только метод get_secret_password_homework невозможно узнать, передали ли мы верный пароль или нет.

По этой причине нам потребуется второй метод, который проверяет правильность нашей авторизованной cookie: https://playground.learnqa.ru/ajax/api/check_auth_cookie

> Если вызвать его без cookie с именем auth_cookie или с cookie, у которой выставлено "неправильное" значение, метод вернет фразу "You are NOT authorized".
> 
> Если значение cookie “правильное”, метод вернет: “You are authorized”

Коллега говорит, что точно помнит свой login - это значение super_admin
А вот пароль забыл, но точно помнит, что выбрал его из списка самых популярных паролей на Википедии (вот тебе и супер админ...).
Ссылка: https://en.wikipedia.org/wiki/List_of_the_most_common_passwords

Искать его нужно среди списка Top 25 most common passwords by year according to SplashData

Итак, наша задача - написать скрипт и указать в нем login нашего коллеги и все пароли из Википедии в виде списка. Программа должна делать следующее:

1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework. В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.

2. Далее эту cookie мы должна передать во второй метод check_auth_cookie. Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный. В этом случае берем следующий пароль и все заново. Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.


### Pytest


**Ex 6: Тест на короткую фразу**

В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести в консоли любую фразу короче 15 символов. А затем с помощью assert проверяет, что фраза действительно короче 15 символов.

Чтобы в переменную получить значение, введенное из консоли, необходимо написать вот такой код:
phrase = input("Set a phrase: ")

Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s": python -m pytest -s my_test.py

**Ex 7: Тест запроса на метод cookie**

Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie

Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert


**Ex 8: Тест запроса на метод header**

Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header

Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert


**Ex 9: User Agent**

User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос. 
Он формируется автоматически клиентом, например браузером. 
Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.

Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check

Метод определяет по строке заголовка User Agent следующие параметры:

>device - iOS или Android
>
>browser - Chrome, Firefox или другой браузер
>
>platform - мобильное приложение или веб
>
>Если метод не может определить какой-то из параметров, он выставляет значение Unknown.

Наша задача написать параметризированный тест. Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения, GET-делать запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.

Список User Agent и ожидаемых значений можно найти по этой ссылке: https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26


**Ex 10: Формирование фреймворка**

На этом уроке мы начали создавать свой фреймворк. 
Он нам пригодится в дальнейшим, так как домашние задания следующего урока будут опираться на методы из этого фреймворка.

Потом эта задача в том, чтобы повторить то, что мы проделали на уроке:

- создать класс BaseCase в директории lib/

- создать класс Assertions в директории lib/

- создать тест TestUserAuth в директории tests/ 


**Ex 11: Тесты на метод user**

В соответствующем классе TestUserRegister необходимо написать больше тестов на создающий пользователя POST-метод: https://playground.learnqa.ru/api/user/

Список тестов:

Создание пользователя с некорректным email - без символа @

Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить, что отсутствие любого параметра не дает зарегистрировать пользователя

Создание пользователя с очень коротким именем в один символ

Создание пользователя с очень длинным именем - длиннее 250 символов


*Ex 12: Запрос данных другого пользователя*

На занятиях в классе TestUserGet мы писали тест на запрос, показывающий данные пользователя. Мы покрыли тестами два кейса:

неавторизованный запрос на данные - там мы получили только username

авторизованный запрос - мы были авторизованы пользователем с ID 2 и делали запрос для получения данных того же пользователя, в этом случае мы получали все поля

В этой задаче нужно написать тест, который авторизовывается одним пользователем, но получает данные другого (т.е. с другим ID). И убедиться, что в этом случае запрос также получает только username, так как мы не должны видеть остальные данные чужого пользователя.


*Ex 13: Негативные тесты на PUT*

На занятиях мы написали только позитивный тест на PUT-метод редактирования пользователя. Давайте напишем несколько негативных:

Попытаемся изменить данные пользователя, будучи неавторизованными
Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ


*Ex 14: Тесты на DELETE*

У нас есть метод, который удаляет пользователя по ID - DELETE-метод https://playground.learnqa.ru/api/user/{id} Само собой, удалить можно только того пользователя, из-под которого вы авторизованы. Необходимо в директории tests/ создать новый файл test_user_delete.py с классом TestUserDelete.

Там написать следующие тесты.

Первый - на попытку удалить пользователя по ID 2. Его данные для авторизации:

    data = {

        'email': 'vinkotov@example.com',

        'password': '1234'

    }
Убедиться, что система не даст вам удалить этого пользователя.

Второй - позитивный. Создать пользователя, авторизоваться из-под него, удалить, затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.

Третий - негативный, попробовать удалить пользователя, будучи авторизованными другим пользователем.


*Ex14: Теги Allure*

Давайте добавим больше Allure-тегов во все написанные нами тесты. Выбирайте любые, которые понравятся из официальной документации - https://docs.qameta.io/allure/

Цель задания - поэкспериментировать с бОльшим количеством тегов, узнать, где именно в отчете они отображаются. В этом задании не будет правильных и неправильных результатов. Но все же нам очень интересно посмотреть, какие теги вы сочтете особенно полезными для вашего фреймворка.
