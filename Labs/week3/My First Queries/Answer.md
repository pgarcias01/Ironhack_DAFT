![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | My First Queries

Open the PgAdmin server from PostgreSQL - pgAdmin 4 is a server that runs on a browser, which is pretty good for an easy start. If you haven't already, start a new server by passing the password you've setup. Create a database called **applestore** and use the `dump file` provided to import a database. 

After creating the `applestore` database, right click it and `restore` it. Select the dump file and hopefully pgAdmin will create the database needed for the following exercises.

Use the table to query the data about Apple Store Apps and answer the following questions: 

**1. What are the different genres?**

Shopping, Games, Education, Reference, Business, Social Networking, Food & Drink, Sports, Catalogs, Weather, Book, Music, Entertainment, Medical, Utilities, Travel, Navigation, Photo & Video, Finance, Health & Fitness, News, Productivity, Lifestyle

**2. Which is the genre with the most apps rated?**
The count of ratings an app has received is in the rating_count_tot column.

Games = 52878491 ratings

**3. Which is the genre with most apps?**

Games = 3862 apps


**4. Which is the one with least?**

Catalogs = 10 apps

**5. Find the top 10 apps most rated.**

"Facebook"
"Instagram"
"Clash of Clans"
"Temple Run"
"Pandora - Music & Radio"
"Pinterest"
"Bible"
"Candy Crush Saga"
"Spotify Music"
"Angry Birds"

**6. Find the top 10 apps best rated by users.**

"Plants vs. Zombies HD"
"Flashlight Òã"
"TurboScanã¢ Pro - document & receipt scanner: scan multiple pages and photos to PDF"
"Learn to Speak Spanish Fast With MosaLingua"
"The Photographer's Ephemeris"
"ÐÈSudoku +"
":) Sudoku +"
"King of Dragon Pass"
"Plants vs. Zombies"
"Infinity Blade"

**7. Take a look at the data you retrieved in question 5. Give some insights.**

- In the top 10 most rated, we have a list of popular apps.

- The genre Games have more apps in the list 4 apps

- The first two are social apps

- All apps is free

**8. Take a look at the data you retrieved in question 6. Give some insights.**

- The Plants vs Zombie appears two times on the list in yours two versions 

- We have two games of Sudoku

- We have 6 games in the top 10

- Only one app is free

**9. Now compare the data from questions 5 and 6. What do you see?**

- Games are the most popular genre in both

- For more popular applications it is more difficult to achieve high marks due to high exposure

**10. How could you take the top 3 regarding both user ratings and number of votes?**

"Head Soccer"
"Plants vs. Zombies"
"Sniper 3D Assassin: Shoot to Kill Gun Game"

**11. Do people care about the price of an app?** Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?

Free Apps
rating total count *avg ~= 19749
rating user *avg ~= 3.37

Paid apps
rating total count *avg ~= 4038
rating user *avg ~= 3.7

Conclusion: Free apps are more popular, but the quality of paid apps maybe better then free.

**Bonus: Find the total number of games available in more than 1 language.**

   1660 apps

**Bonus2: Find the number of free vs paid apps**

Free    Paid
4056	3141


**Bonus3: Find the number of free vs paid apps for each genre**

"Genre" 	Free 	Paid  
"Shopping"	121	1
"Games"	2257	1605
"Education"	132	321
"Reference"	20	44
"Business"	20	37
"Social Networking"	143	24
"Food & Drink"	43	20
"Sports"	79	35
"Catalogs"	9	1
"Weather"	31	41
"Book"	66	46
"Music"	67	71
"Entertainment"	334	201
"Medical"	8	15
"Utilities"	109	139
"Travel"	56	25
"Navigation"	20	26
"Photo & Video"	167	182
"Finance"	84	20
"Health & Fitness"	76	104
"News"	58	17
"Productivity"	62	116
"Lifestyle"	94	50


## Deliverables 
You need to submit a `.sql` file that includes the queries used to answer the questions above, as well as an `.md` file including your answers. 
