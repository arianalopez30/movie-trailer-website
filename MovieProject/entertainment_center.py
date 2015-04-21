
#-----------------------------------
#Imports
#-----------------------------------
import media
import fresh_tomatoes

#creating instance of movie for Train Wreck
train_wreck = media.Movie("Trainwreck",
                        "About a girls dating life",
                        "http://upload.wikimedia.org/wikipedia/en/c/c5/Trainwreck_poster.jpg",
                        "https://www.youtube.com/watch?v=bLlpLUUn-5E")
#creating instance of movie for How to train your dragon
dragon = media.Movie("Train Your Dragon 2",
                        "A young Viking and his Dragon Toothless must defend their dragons",
                        "http://ia.media-imdb.com/images/M/MV5BMzMwMTAwODczN15BMl5BanBnXkFtZTgwMDk2NDA4MTE@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=Z9a4PvzlqoQ")

#creating instance of movie for Book of Life
book_of_life = media.Movie("Book of Life",
                       "Manolo, a young man who is torn between fulfilling the expectations of his family and following his heart, embarks on an adventure that spans three fantastic worlds where he must face his greatest fears.",
                        "http://ia.media-imdb.com/images/M/MV5BMTkzOTgzNDYzOF5BMl5BanBnXkFtZTgwOTgxMTkyMjE@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=NBw5YScs8iQ")

#creating instance of movie for animated movie Home
home = media.Movie("Home",
                   "An alien on the run from his own people, lands on Earth and makes friends with the adventurous Tip, who is on a quest of her own.",
                   "http://media.aintitcool.com/media/uploads/2015/muldoon/home_poster.jpg",
                   "https://www.youtube.com/watch?v=MyqZf8LiWvM")

#creating instance of movie for Jaws
jaws = media.Movie("Jaws",
                        "When a gigantic great white shark begins to menace the small island community of Amity, a police chief, a marine scientist and grizzled fisherman set out to stop it.",
                        "http://www.vintage-poster-art.com/wp-content/uploads/2014/12/Jaws-movie-poster.jpg",
                        "https://www.youtube.com/watch?v=ucMLFO6TsFM")
#creating instance of movie for Rocky
rocky = media.Movie("Rocky",
                        "Rocky Balboa, a small-time boxer gets a supremely rare chance to fight the heavy-weight champion, Apollo Creed, in a bout in which he strives to go the distance for his self-respect.",
                        "https://www.movieposter.com/posters/archive/main/90/MPW-45270",
                        "https://www.youtube.com/watch?v=7RYpJAUMo2M")
#put all objects in an array
movies = [train_wreck, dragon, book_of_life, jaws, rocky, home]

#movies = [train_wreck, dragon, jaws, rocky, home]

#Call the tomatoes class and pass it the array movies...it will consolidate
#all of the movies on one page
fresh_tomatoes.open_movies_page(movies)
