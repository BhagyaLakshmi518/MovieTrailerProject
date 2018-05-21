print("Content-type:text/html \n")
import media
import fresh_tomatoes

deadpool=media.Movie("deadpool 2","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd39RpQm8W3K_yC8bnb8wJqGzYbkP03mF8z_CK2NpECCjapOAV",
              "https://www.youtube.com/embed/D86RtevtfrA"
              )
kaala=media.Movie("kaala",
              "https://i.ytimg.com/vi/BCCbpfKl_LM/maxresdefault.jpg","https://www.youtube.com/embed/Wm_vSSlVsV4")
blackpanther=media.Movie("blackpanther",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkN8SlAyVUaJz0rv_wVAxGWsJmzg5L1Tnqk15lDWBFQwikFdFD",
                  "https://www.youtube.com/embed/xjDjIWPwcPU")
bangloredays=media.Movie("Chalo",
              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_Cdvtj5TQnS4_JN04J61upyGZhvPtUpfj-qz8gkg7VvrrKQOt",
              "https://www.youtube.com/embed/Gdzif0Px_qY"
              )
band=media.Movie("Band Baaja Baarat",
                 "https://www.yashrajfilms.com/images/default-source/Movies/Band-Baaja-Baaraat/band-baaja-baaraat_tablet.jpg?sfvrsn=4",
                 "https://www.youtube.com/embed/k67ErU7SeIE")
movies=[deadpool,kaala,blackpanther,bangloredays,band]
fresh_tomatoes.open_movies_page(movies)
