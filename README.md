# capstone-1

My first capstone project.

I'd like to create a website similar to ballchasing.com, using their api. I will be writing all the code in python/html. 
I'm attempting to get as many features in the project as possible within a week.

*The included api key is neceassry for the app to work.

api: https://ballchasing.com/doc/api#top


*1 week later*

I haven't deployed the site, and there are still some features I'd like to implement. This is what I have now, though.

The website is similar to a real website, ballchasing.com. Ballchasing.com accepts user file uploads called "replays" from a video game named "Rocket league". It then returns a bunch of information thats contained in the file. This includes player names, dates, goals, etc, etc. There is a ton of data. 

My website returns three things. 

1. Replays. The latest 10000 replays get presented
2. Pro replays. Only the latest 10000 replays from professional players get displayed
3. Player search. This feature lets the user put in a name, and if that name is in any replay file (up to 10000 replays) it gets returned. 

I chose these features because they were easy to implement, and this is my first true website. 
The main tool I used was flask. I used python for most of the logic, and a ton of html to display different pages. There is a tiny amount of JS in the htmls to render the replay data.

Organizing the data is still unfinished for now. Using something like json vue makes the data slightly easier to read. 
I would like to finish this in the future. 
