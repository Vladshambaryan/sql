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
SELECT email
FROM giveaway 
ORDER BY total_amount DESC
limit 5
==
SELECT player_name, set_1 + set_2 + set_3 AS TOTAL  # выбрать имена игроков и общее количество очков как Total
FROM matches
==
SELECT title, genre, rating  # выбрать title, genre и rating фильтровать по genre 'Action' упорядочить по rating
FROM movies
WHERE genre = 'Action' 
ORDER BY rating DESC 
==
SELECT name, price  # выбрать name десерта и price где название содержит 'chocolate'
FROM desserts
WHERE name LIKE 'chocolate%'
==
SELECT title, artist # выбрать title песни и artist из таблицы songs где title песни содержит слово 'love' и упорядочьте результаты по убыванию рейтинга
FROM songs
WHERE title LIKE '%Love%'
ORDER by rating DESC 
==
SELECT make, model, price_per_day  # table name: cars выбрать make машины, model и price per day где цена за день меньше или равна $100
FROM cars
WHERE price_per_day <= 100
==
SELECT name, price, discount  # таблицa: productsвыбрать name, price и discount где скидка больше 0 упорядочить по убыванию price discount
FROM products
WHERE discount > 0
ORDER BY discount DESC 
==
SELECT topic, sum(likes)   # таблицa: posts извлечь сумму likes для каждой темы
FROM posts
GROUP by topic
==
SELECT DISTINCT subject   # таблицa: teachers выбрать уникальные subjects в школе
FROM teachers
GROUP by subject
==
SELECT name, surname   # таблицa: orders выбрать имя, фамилию тех, кто имеет идентификатор ticket и сидит в рядах 1-5
FROM orders
WHERE pre_book = true and seat_num is NOT NULL 
==
SELECT team, AVG(goals)   # таблицa: games вычислить среднее количество забитых голов для каждой команды во время игр в Miami
FROM games
WHERE city = 'Miami'
GROUP BY team
==
UPDATE students SET name = 'Donald' 
WHERE name = 'VLADIMIR'
==
insert into `groups` (title, start_date, end_date) 
VALUES ('QA testers', 'oct 2024', 'feb 2025')
==
insert into books (title, taken_by_student_id) 
VALUES ('Python3', 3263)
==
SELECT * 
FROM students JOIN books 
on students.id = books.taken_by_student_id 
--  Этот SQL-запрос выполняет внутреннее соединение (JOIN) двух таблиц: students и books,
--  используя поле id из таблицы students и поле taken_by_student_id из таблицы books. 
--  Результат будет включать строки, где значение students.id соответствует значению 
--  books.taken_by_student_id, то есть он покажет всех студентов и книги, которые были взяты ими.
==
SELECT * 
FROM students 
LEFT JOIN books 
on students.id = books.taken_by_student_id 
-- Этот SQL-запрос делает выборку всех записей из таблицы students, при этом выполняется левое соединение 
-- с таблицей books на основании того, что поле students.id соответствует полю books.taken_by_student_id.
-- Если студент взял книгу (то есть есть соответствие по taken_by_student_id), то информация о книге будет включена.
-- Если студент не брал книг, данные по нему все равно будут в результате, но поля из таблицы books будут заполнены 
-- значением NULL.
==
SELECT * 
FROM students 
RIGHT JOIN books 
on students.id = books.taken_by_student_id 
-- Этот SQL-запрос выполняет выборку всех записей из таблицы books и присоединяет к ним соответствующие 
-- записи из таблицы students с помощью правого соединения (RIGHT JOIN) по условию, что поле students.id 
-- соответствует полю books.taken_by_student_id.
-- Все записи из таблицы books.
-- Если студент взял книгу (то есть есть соответствие по taken_by_student_id), информация о студенте будет 
-- включена.
-- Если книга не была взята студентом (нет соответствующего student.id), данные о студенте будут NULL.
==
-- Все оценки студента
-- Выбираем имя, фамилию студента, значение оценки и ID занятия
SELECT students.name, students.second_name, marks.value, marks.lesson_id
FROM students
-- Соединяем таблицу marks с таблицей students по полю student_id
LEFT JOIN marks on students.id = marks.student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с именем "Donald" и фамилией "Trump"
WHERE name = 'Donald'
AND second_name = 'Trump'
==
-- Все книги, которые находятся у студента
-- Выбираем имя, фамилию студента и название книги
SELECT students.name, students.second_name, books.title
FROM students
-- Соединяем таблицу books с таблицей students по полю taken_by_student_id
LEFT JOIN books on students.id = books.taken_by_student_id
-- Фильтруем результаты, чтобы выбрать записи только для студента с именем "Donald" и фамилией "Trump"
WHERE students.name = 'Donald' AND students.second_name = 'Trump'
==
SELECT students.name, students.second_name, `groups`.title AS group_title, `groups`.start_date, `groups`.end_date, 
       subjets.title AS subject_title, lessons.title AS lesson_title, lessons.subject_id, 
       marks.value AS mark_value, marks.lesson_id, books.title AS book_title
FROM students
LEFT JOIN `groups` ON students.group_id = `groups`.id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
LEFT JOIN books ON students.id = books.taken_by_student_id
WHERE students.name = 'Donald' AND students.second_name = 'Trump';
==












 
 

          
          
        
          
          













  
