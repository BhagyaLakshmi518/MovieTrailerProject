import webbrowser
print("Content-type:text/html \n")
"""class for Movie representation"""


class Movie():
    VALID_RATINGS = ['EXCELLENT', 'GOOD', 'BAD', 'AVERAGE']

    """movie_title=a string for representing title of the movie
       poster_image = a string containing a image url
       trailer_youtube = a string containing youtube trailer of
       the respective movie
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
