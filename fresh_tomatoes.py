import re
import os
import webbrowser
print("Content-type:text/html \n")


main_page_head = '''
<DOCTYPE html>
<html>
<head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
.a,.b,.c,.d,.e{
  width:300px;
  height:400px;
  float:left;
  margin-left:50px;
  margin-top:20px;
  padding:20px
}
img{
      width:100%;
      height:100%;
     /* overflow: hidden;*/
}
.a:hover{
  background-color:lightcoral;
}
.b:hover{
  background-color: lavender;
}
.c:hover{
  background-color: burlywood;
}
.d:hover{
  background-color:yellowgreen;
}
.e:hover{
  background-color:lightseagreen;
}
.overlay {
  position: relative;
  bottom: 30px;
  background: rgb(0, 0, 0);
  background: rgba(0, 0, 0, 0.5); /* Black see-through */
  color: #f1f1f1;
  transition: .5s ease;
  opacity:0;
  color: white;
  font-size: 20px;
  padding: 10px;
  text-align: center;
}
.a:hover .overlay {
  opacity: 1;
}
.b:hover .overlay {
  opacity: 1;
}
.c:hover .overlay {
  opacity: 1;
}
.d:hover .overlay {
  opacity: 1;
}
.e:hover .overlay {
  opacity: 1;
}
a{
  color:white;
}
h1
{
   text-align:center;
   color:red;
}
</style>
<script src="https://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256"
            "-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin="anonymous"></script>
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/"
                   "bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/"
       "bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myModal").on("hidden.bs.modal", function () {
                $("#iframeYoutube").attr("src", "#");
            })
        })
        function changeVideo(vId) {
            var iframe = document.getElementById("iframeYoutube");
            iframe.src = "https://www.youtube.com/embed/" + vId;
            $("#myModal").modal("show");
        }
    </script>
</head>'''


main_page_content = '''
<body style="background-color:brown;">
<h1 style="color:blue;">MOVIE TRAILERS</h1>
<div class="a" onclick=" changeVideo('20bpjtCbCz0')">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd39RpQ"
          "m8W3K_yC8bnb8wJqGzYbkP03mF8z_CK2NpECCjapOAV"/>
<div class="overlay">Dead Pool2</div>
</div>
<div class="b" onclick=" changeVideo('Wm_vSSlVsV4')">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUwRKWuYYh"
  "NHCFxhdB2MqmhZHQ9ZQL-SrDrtWSlp51cHbDFgG51A"/>
<div class="overlay">Kaala</div>
</div>
<div class="c" onclick=" changeVideo('xjDjIWPwcPU')">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNb8BPjnh1_"
         "8Pxta0HHedtiuT8rR8a6IDbk9elEpzsgvTbtWnu7w"/>
<div class="overlay">BlackPanther</div>
</div>
<div class="d" onclick=" changeVideo('Gdzif0Px_qY')">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdGcVcHwBiYd"
         "5HGzUbYsKE3QYg8v4F3VJ3_4odLUc9TEBoDBVi"/>
<div class="overlay">Chalo</div>
</div>
<div class="e" onclick=" changeVideo('k67ErU7SeIE')">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaI0WvPhZ"
            "h7n6zhcFH8VzJ_TQFtDln9fKhkEpciXD7sdv16TtfdQ"/>
    <div class="overlay">Band Baja Baarat</div>
</div>
<div class="modal fade" id="myModal" tabindex="-1"
           aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-body">
                    <iframe id="iframeYoutube" width="555" height="350"
                             src="" frameborder="0" ></iframe>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default"
                         data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

movie_title_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer-yutube-
id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}"width="220" height="342">
    <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_url = (youtube_id_match.group(0) if youtube_id_match
                               else None)
        content += movie_title_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_url
            )
        return content


def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = main_page_content.format(
        movie_tiles=create_movie(movies)
        )
    output_file.write(main_page_head+rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
        
