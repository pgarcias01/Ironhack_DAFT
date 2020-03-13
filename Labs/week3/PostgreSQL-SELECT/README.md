![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | PostgreSQL Select

## Introduction

In this lab you will practice how to use the PostgreSQL `SELECT` statement which will be extremely useful in your future work as a data analyst/scientist/engineer. **You will use the `publications` database**. You can find it in the Lab card on Student Platform. Use your database management application to query it. 

You will create a `solutions.sql` file to record your solutions to all challenges.

## Challenge 1 - Who Have Published What At Where?

In this challenge you will write a PostgreSQL `SELECT` query that joins various tables to figure out what titles each author has published at which publishers. Your output should have at least the following columns:

* `AUTHOR ID` - the ID of the author
* `LAST NAME` - author last name
* `FIRST NAME` - author first name
* `TITLE` - name of the published titlec  
* `PUBLISHER` - name of the publisher where the title was published

Your output will look something like below:

![Challenge 1 output](./images/challenge-1.png)

*Note: the screenshot above is not the complete output.*

If your query is correct, the total rows in your output should be the same as the total number of records in Table `titleauthor`.

## Challenge 2 - Who Have Published How Many At Where?

Elevating from your solution in Challenge 1, query how many titles each author has published at each publisher. Order your output by the title count in descending order. Your output should look something like below:

![Challenge 2 output](./images/challenge-2.png)

*Note: the screenshot above is not the complete output.*

To check if your output is correct, sum up the `TITLE COUNT` column. The sum number should be the same as the total number of records in Table `titleauthor`.

*Hint: In order to count the number of titles published by an author, you need to use [COUNT](https://www.w3resource.com/PostgreSQL/postgresql-count-function.php). Also check out [Group By](https://www.w3resource.com/PostgreSQL/postgresql-group-by.php) because you will count the rows of different groups of data.*

## Challenge 3 - Best Selling Authors

Who are the top 3 authors who have sold the highest number of titles? Write a query to find out.

Requirements:

* Your output should have the following columns:
	* `AUTHOR ID` - the ID of the author
	* `LAST NAME` - author last name
	* `FIRST NAME` - author first name
	* `TOTAL` - total number of titles sold from this author
* Your output should be ordered based on `TOTAL` from high to low.
* Only output the top 3 best selling authors.

## Challenge 4 - Best Selling Authors Ranking

Now modify your solution in Challenge 3 so that the output will display all 23 authors instead of the top 3. Note that the authors who have sold 0 titles should also appear in your output (ideally display `0` instead of `NULL` as the `TOTAL`). Also order your results based on `TOTAL` from high to low.

## Deliverables

* `solution.sql` that contains all your MySQL queries.

## Submission

* Add `solutions.sql` to git.
* Commit your code.
* Submit (push) your solution to your github.