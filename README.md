# MovieTrailerProject
#This project is for people who are intrested in watching movie trailers.
#My website consits of different movie posters and on clicking on them we get the youtube trailer on the same page itself. 
#I craeted this website using three python files named as media.py,entertainment_center.py,fresh_tomatoes.py.
#My website runs by running the entertainment_center.py page.
#In entertainment_center.py I pass the arguments like movie_title,movie_poster and youtube url respectively to the "Movie" class which is present in the media.py file.
#We store the values of different movies in different variables.
#We pass all these variables to open_movies_page() function which is present in the fresh_toamtoes.py file.
#upon calling the open_movies_page() in the fresh_tomatoes.py it creates a html page called fresh_tomatoes.html which opens our main movietrailes page based on the content we attached in the fresh_tomatoes.py file.
#On calling the Movie class we automatically call the constructor "init" which stores the values of the parameters in different variables.It also calls the Show_tailer class in order to display the youtube trailer.
#I uploaded these files in my github account.
