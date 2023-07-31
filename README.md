# Проект по тестированию сайта Reqres.ru
> <a target="_blank" href="https://reqres.in/">Ссылка на сайт</a>

![This is an image](images/screenshots/reqres.png)

<!-- Технологии -->
### Проект реализован с использованием:
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
</p>

<!-- Тест кейсы -->

### Что проверяем
✓ Запрос списка пользователей  
✓ Создание пользователя при вводе валидных данных  
✓ Получаение пользователя по переданному id  
✓ Обновление пользователя  
✓ Удаление пользователя  
✓ Ошибка авторизации с пустым обязательным полем password  


### <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/Okuneva_Reqres_API_tests/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение.
![This is an image](images/screenshots/jenkins.png)

<!-- Allure report -->
## Локальный запуск автотестов
Пример командной строки:
```bash
pytest .
```

Получение отчёта:
```bash
allure.bat serve
```
<!-- Allure TestOps -->


### <img width="5%" title="Allure Report" src="images/logo/allure_report.png"> Allure report.
### [Report](https://jenkins.autotests.cloud/job/Okuneva_Reqres_API_tests/2/allure/)
##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/AllureReport.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены Request curl и Response Body
![This is an image](images/screenshots/AllureSuites.png)


<!-- Allure TestOps -->

### <img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/3562/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshots/AllureTestOps.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira

![This is an image](images/screenshots/TestCases.png)


<!-- Jira -->

### <img width="5%" title="Jira" src="images/logo/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/Jira.png)




