import media
import fresh_tomatoes

deer_hunter = media.Movie(
		"The Deer Hunter",
		"Fun in 'nam",
		"https://upload.wikimedia.org/wikipedia/en/5/57/The_Deer_Hunter_poster.jpg",
		"https://www.youtube.com/watch?v=SKHZ5-JThFE")

bone_tomahawk = media.Movie(
		"Bone Tomahawk",
		"Creepy Western",
		"https://upload.wikimedia.org/wikipedia/en/9/9c/Bone_Tomahawk_Poster.jpg",
		"https://www.youtube.com/watch?v=0ZbwtHi-KSE")

idiocracy = media.Movie(
		"Idiocracy",
		"Scary vison of the future",
		"https://upload.wikimedia.org/wikipedia/en/6/6b/Idiocracy_movie_poster.jpg",
		"https://www.youtube.com/watch?v=BBvIweCIgwk")

interstellar = media.Movie(
		"Interstellar",
		"Earth dies, we find a worm hole",
		"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
		"https://www.youtube.com/watch?v=0vxOhd4qlnA")

cannibal = media.Movie(
		"Cannibal! The Musical",
		"The true story of Alfred Packer",
		"http://vignette2.wikia.nocookie.net/to-hollywood-and-beyond/images/6/6a/Cannibal!_The_Musical.jpg/revision/latest?cb=20150508004834",
		"https://www.youtube.com/watch?v=8GszhYsV3MM")

good_dinosaur = media.Movie(
		"The Good Dinosaur",
		"Dinosaur gets lost and takes human child as a pet",
		"https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
		"https://www.youtube.com/watch?v=O-RgquKVTPE") 
# List of movies to be fed through the open_movies_page operator inside
# the fresh_tomatoes class
movies = [deer_hunter, bone_tomahawk, idiocracy, interstellar, cannibal, 
		  good_dinosaur]

# runs the program
fresh_tomatoes.open_movies_page(movies)
