#**Movie Trailer Website**

This website is for the <strong>movies and their trailer</strong> to be viewed.

##Website content

*Box art imagery of the movies (you can find cool movies [here]
(file:///E:/fresh_tomatoes.html))
*Movie trailer link

## Steps to run the application
*From the movies folder find the python file 'entertainment_center.py' and run the file.
*Look for the website that is launched and click on the Box art to view the trailer of that movie.


## Code of the class Movie

Sample code of the Movie class:
```
import webbrowser

class Movie():
	"""docstring for Movie"""
	#valid_ratings = ["G", "PG", "PG-13", "R"]
	
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
```

<!--- referred Udacity course on readme to design readme--> 
