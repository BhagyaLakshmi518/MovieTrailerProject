# MovieTrailerProject
#This project is for people who are intrested in watching movie trailers.
#My website consits of different movie posters and on clicking on them we get the youtube trailer on the same page itself. 
#I created this website using three python files named as media.py,entertainment_center.py,fresh_tomatoes.py.
#My website runs by running the entertainment_center.py page.
#The entertainment_center.py consists the following code:
   #moviename = media.Movie("movie_title",
                       "poster image_url"
                       "youtube_trailer_url"
                       )
#In entertainment_center.py I pass the arguments like movie_title,movie_poster image_url and youtube url respectively to the "Movie" class which is present in the media.py file.
#Whenever I call the Movie() class for a new movie from the entertainment_center.py file a constructor method is called named __init()__ #by default.
#I store the values of different movies in different variables.
#The init method in the media.py file is as follows:
      #def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#The __init__() method stores the passed arguments in appropriate variables for further use.
#I store all the variables that store the details of the movies in an array named movies[].
#The movies[] array is then passed as argument for the function open_movies_page() present in the fresh_tomatoes.py file.
#Upon calling the open_movies_page() in the fresh_tomatoes.py it creates a html page called fresh_tomatoes.html which opens our main         movietrailes page based on the content we attached in the fresh_tomatoes.py file.
#On calling the Movie class we automatically call the constructor "init" which stores the values of the parameters in different variables.It also calls the Show_tailer class in order to display the youtube trailer.
#I uploaded these files in my github account.
#You can view my files containing these codes using the following link:
      https://github.com/BhagyaLakshmi518/MovieTrailerProject.git
