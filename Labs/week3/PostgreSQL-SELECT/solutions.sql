--Challenge 1 - Who Have Published What At Where?

--show ALL from table authors

SELECT * FROM authors;

--show All from titleauthor

SELECT * FROM titleauthor;

--show All from titles:

SELECT * FROM titles;

--show All from publishers:

SELECT * FROM publishers;

-- do the select with inner join

SELECT a.au_id AS "AUTHOR ID", a.au_lname AS "LAST NAME", a.au_fname AS "FIRST NAME", c.title AS "TITLE", d.pub_name AS "PUBLISHER"
	FROM authors AS a
		INNER JOIN
		titleauthor as b
		ON a.au_id = b.au_id
		INNER JOIN
		titles as c
		ON b.title_id = c.title_id
		INNER JOIN
		publishers as d
		ON c.pub_id = d.pub_id
		ORDER BY "AUTHOR ID";
		
--Challenge 2 - Who Have Published How Many At Where?

--show ALL from table authors

SELECT * FROM authors;

--show All from titleauthor

SELECT * FROM titleauthor;

--show All from titles:

SELECT * FROM titles;

--show All from publishers:

SELECT * FROM publishers;

-- do the select with inner join

SELECT a.au_id AS "AUTHOR ID", a.au_lname AS "LAST NAME", a.au_fname AS "FIRST NAME", d.pub_name AS "PUBLISHER", COUNT(c.title) AS "TITLE COUNT" 
	FROM authors AS a
		INNER JOIN
		titleauthor as b
		ON a.au_id = b.au_id
		INNER JOIN
		titles as c
		ON b.title_id = c.title_id
		INNER JOIN
		publishers as d
		ON c.pub_id = d.pub_id
		GROUP BY a.au_id, a.au_lname, a.au_fname, d.pub_name
		ORDER BY "TITLE COUNT" DESC;
		
--Who are the top 3 authors who have sold the highest number of titles?

--show ALL from table authors

SELECT * FROM authors;

--show All from titleauthor

SELECT * FROM titleauthor;

--show All from sales

SELECT * FROM sales;

-- do the select with inner join

SELECT a.au_id AS "AUTHOR ID", a.au_lname AS "LAST NAME", a.au_fname AS "FIRST NAME", SUM(d.qty) AS "TOTAL"
	FROM authors AS a
		INNER JOIN
		titleauthor as b
		ON a.au_id = b.au_id
		INNER JOIN
		sales as d
		ON b.title_id = d.title_id
		GROUP BY a.au_id, a.au_lname, a.au_fname
		ORDER BY "TOTAL" DESC LIMIT 3;
		
--Challenge 4 - Best Selling Authors Ranking

--show ALL from table authors

SELECT * FROM authors;

--show All from titleauthor

SELECT * FROM titleauthor;

--show All from sales

SELECT * FROM sales;

-- do the select with inner join

SELECT a.au_id AS "AUTHOR ID", a.au_lname AS "LAST NAME", a.au_fname AS "FIRST NAME", COALESCE(SUM(d.qty), 0) AS "TOTAL"
	FROM authors AS a
		LEFT JOIN
		titleauthor as b
		ON a.au_id = b.au_id
		LEFT JOIN
		sales as d
		ON b.title_id = d.title_id
		GROUP BY a.au_id, a.au_lname, a.au_fname
		ORDER BY "TOTAL" DESC