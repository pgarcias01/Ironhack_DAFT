--1. What are the different genres?**

SELECT DISTINCT prime_genre
  FROM data;
 
--2. Which is the genre with the most apps rated?**

SELECT prime_genre, SUM(rating_count_tot) AS rating FROM DATA 
	GROUP BY prime_genre 
		ORDER BY rating DESC;
		
--3. Which is the genre with most apps?

SELECT prime_genre, COUNT(prime_genre) AS qtd FROM data
	GROUP BY prime_genre 
		ORDER BY qtd DESC;
		
--4. Which is the one with least?**

SELECT prime_genre, COUNT(prime_genre) AS qtd FROM data
	GROUP BY prime_genre 
		ORDER BY qtd;
		
--5. Find the top 10 apps most rated

SELECT * FROM data 
	ORDER BY rating_count_tot DESC
		LIMIT 10;
		
--6. Find the top 10 apps best rated by users.**

SELECT * FROM data 
	ORDER BY user_rating DESC
		LIMIT 10;
		
--10. How could you take the top 3 regarding both user ratings and number of votes?**

SELECT * FROM data 
	ORDER BY user_rating DESC, rating_count_tot DESC
		LIMIT 3;
		
--11. Do people care about the price of an app?**

--Calculate avg rating and count rating from free apps
SELECT AVG(rating_count_tot) as avg_num_rat, AVG(user_rating) as avg_rag
	FROM data
		WHERE price = 0;
		
--Calculate avg rating and count rating from free apps
SELECT AVG(rating_count_tot) as avg_num_rat, AVG(user_rating) as avg_rag
	FROM data
		WHERE price > 0;
		
--Bonus: Find the total number of games available in more than 1 language.**

SELECT COUNT(*) FROM DATA
	WHERE "lang.num" > 1 and prime_genre = 'Games';
	
--Bonus2: Find the number of free vs paid apps**

SELECT COUNT(*) filter (where price = 0) as free_apps,
	   COUNT(*) filter (where price > 0) as paid_apps 
	   FROM data;

--Bonus3: Find the number of free vs paid apps for each genre

SELECT prime_genre,
	   COUNT(*) filter (where price = 0) as free_apps,
	   COUNT(*) filter (where price > 0) as paid_apps 
	   FROM data
	   GROUP BY prime_genre;