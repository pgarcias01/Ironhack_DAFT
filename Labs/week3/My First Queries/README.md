![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | My First Queries

Open the PgAdmin server from PostgreSQL - pgAdmin 4 is a server that runs on a browser, which is pretty good for an easy start. If you haven't already, start a new server by passing the password you've setup. Create a database called **applestore** and use the `dump file` provided to import a database. 

After creating the `applestore` database, right click it and `restore` it. Select the dump file and hopefully pgAdmin will create the database needed for the following exercises.

Use the table to query the data about Apple Store Apps and answer the following questions: 

**1. What are the different genres?**

**2. Which is the genre with the most apps rated?**
The count of ratings an app has received is in the rating_count_tot column.

**3. Which is the genre with most apps?**

**4. Which is the one with least?**

**5. Find the top 10 apps most rated.**

**6. Find the top 10 apps best rated by users.**

**7. Take a look at the data you retrieved in question 5. Give some insights.**

**8. Take a look at the data you retrieved in question 6. Give some insights.**

**9. Now compare the data from questions 5 and 6. What do you see?**

**10. How could you take the top 3 regarding both user ratings and number of votes?**

**11. Do people care about the price of an app?** Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?

**Bonus: Find the total number of games available in more than 1 language.**

**Bonus2: Find the number of free vs paid apps**

**Bonus3: Find the number of free vs paid apps for each genre**


## Deliverables 
You need to submit a `.sql` file that includes the queries used to answer the questions above, as well as an `.md` file including your answers. 
