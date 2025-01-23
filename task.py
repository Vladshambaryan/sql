Структура данных:
Реляционные базы данных (SQL): Данные хранятся в виде таблиц, где строки представляют записи, а столбцы — атрибуты. 
Все таблицы связаны друг с другом через ключи (первичные и внешние). 
Строгая схема задает типы данных и их взаимосвязи.
Нереляционные базы данных (NoSQL): Данные могут храниться в виде документов, ключ-значение, графов или столбцов. 
Такие базы данных более гибкие, не требуют строгой схемы, что позволяет хранить данные в произвольных структурах, например, JSON
==
Реляционные базы данных: Используют язык SQL для выполнения запросов, который ориентирован на работу с таблицами, присоединение данных,
фильтрацию, агрегацию и прочие операции.
Нереляционные базы данных: Для работы с данными применяются специализированные языки запросов или API, которые могут быть более простыми 
или более сложными, в зависимости от модели хранения данных.
==
Использование:
Реляционные базы данных: Хорошо подходят для приложений с четко определенной структурой данных и сложными запросами, 
такими как ERP-системы, банковские системы.
Нереляционные базы данных: Часто применяются в системах с большим объемом неструктурированных данных, таких как социальные сети,
системы мониторинга, big data проекты.
Примеры реляционных БД: MySQL, PostgreSQL, Oracle. Примеры нереляционных БД: MongoDB, Cassandra, Redis.
  ==
SELECT year
FROM movies
  ==
 SELECT tiitle
FROM movies 
  ==
 SELECT id, name
FROM products
  ==
  SELECT *
FROM departments
  ==
SELECT * 
FROM movies ORDER BY year
  ==
SELECT *
FROM costomers
Order by age DESC
  ==
 SELECT *
FROM costomers
Order by age ASC
  ==
SELECT *      # LIMIT используется для пропуска уменьшения количества записей
FROM emploers 
LIMIT 10 
  ==
 SELECT *     #  Сортирует записи в порядке убывания (от наибольшего значения к наименьшему)
FROM products 
ORDER BY price DESC LIMIT 10 #  Ограничивает результат выборки 10 первыми строками 
  ==
SELECT title
FROM movies
LIMIT 1 OFFSET 1 # OFFSET пропуск
 ==
  SELECT * 
  FROM products 
  DESC  LIMIT 5
  ==
SELECT name, prise * delivery
FROM sales
  ==
SELECT * 
FROM studio 
WHERE name = "walt Disney"
  ==
SELECT title
FROM movies 
WHERE gear > 2000          
  ==
SELECT * 
FROM songs 
WHERE length > 3 
  ==
SELECT  name , prise 
FROM desserts 
WHERE name LIKE '% chocolate%'  
  ==
 SELECT name, email
FROM user 
WHERE status = 'active'         
  ==
SELECT name 
FROM students 
WHERE country = 'USA' 
  ==
SELECT * 
FROM " books" 
WHERE genre = ' Fiction ' 
  ==
 SELECT titles 
 FROM books 
 WHERE category = "novel" 
 ==
 SELECT titles 
 FROM books 
 WHERE year = 2000
 ==
 SELECT name 
 FROM products 
 WHERE quantity <>0;
 ==
 SELECT title 
 FROM books 
 WHERE LOWER (title) LIKE '%robots%'; # Можно использовать UPPER и LOWER для поиска без учета регистра.
 ==
SELECT MIN(year)
FROM movies;
==
SELECT MAX(year)
FROM movies;
==
SELECT COUNT (число) # Подсчитывает количество записей
FROM movies;
COUNT()
==
SELECT SUM (price) # Вычисляет общую суму значачений
FROM products;
SUM()
==
SELECT AVG (price) # AVG -вычисляет среднее значение
FROM products
==
SELECT SUM (price + delivery) AS revenue # Выберите сумму цена + доставка доход изпродаж где стататус завешеный
FROM sales 
WHERE status = " completed  "
==
SELECT genre, AVG (budget) # Выбор жанра средний бюджет из фильмов сгрупированых по  жанру
FROM movies
GROUP BY genre;
==
SELECT topic, SUM (LIKES) # Извлеч сумму лайков для каждой теммы
FROM posts 
GROUP BY topic 
==
SELECT product, MAX(price)
FROM sales
WHERE city = 'NEW YORK'
GROUP BY products;
==
SELECT department, COUNT(*) # Сгрупировать по депортаменту где зарплаты работников больше 5000
FROM emploees
WHERE salary > 5000
GROUP BY department
==
SELECT class, AVG (scope) # Это фильтр, который оставляет только те строки (классы), у которых средняя оценка выше 85.
FROM students
GROUP BY class
HAVING AVG (scope) > 85
==
SELECT department, AVG (salary) # Это фильтр, который оставляет только те отделы, у которых средняя зарплата превышает 5000.
FROM emploees
GROUP BY department 
HAVING AVG (salary) >5000
==
SELECT DISTINCT name # Ключевое слово DISTINCT означает, что в результате будут только уникальные имена, хранящиеся в таблице
FROM employees;
==
SELECT * 
FROM products 
WHERE category = 'Glothing' OR categoryn = 'Shoes'; # где товары относятся к категории "Одежда" или "Обувь".
==
SELECT *  # извлеч значение не являющиеся null
FROM movies 
WHERE  genre IS NOT NULL 
==
SELECT name   # пользователей, у которых нет информации о прогрессе
FROM users 
WHERE progress IS NULL
==
SELECT *    # записи в таблице, где жанр фильма не указан или не заполнен.
FROM movies 
WHERE genre IS NULL
==
SELECT DISTINCT genre  # То есть, он вернет список всех уникальных жанров фильмов, которые есть в этой таблице, исключая повторяющиеся значения.
FROM movies
==
SELECT *  # Последний с конца
FROM students 
ORDER BY id DESC LIMIT 10
==
SELECT * # второц с конца
FROM students 
ORDER BY id DESC LIMIT 1, 1
==











 
 

          
          
        
          
          













  
