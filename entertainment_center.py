import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
						"A marine on an alien planet",
						"https://en.wikipedia.org/wiki/File:Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

armageddon = media.Movie("Armageddon",
						"A team of expert on a mission to save Earth from extinction",
						"https://en.wikipedia.org/wiki/Armageddon_(1998_film)#/media/File:Armageddon-poster06.jpg",
						"https://www.youtube.com/watch?v=iq6q2BrTino")

ratatouille = media.Movie("Ratatouille",
						"A movie of a rat the expert chef",
						"https://en.wikipedia.org/wiki/File:RatatouillePoster.jpg",
						"https://www.youtube.com/watch?v=ALUmKa_mpik")

midnight_in_paris = media.Movie("Midnight in paris",
						"Going back in time to meet authors",
						"https://en.wikipedia.org/wiki/File:Midnight_in_Paris_Poster.jpg",
						"https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
						"A really real reality show",
						"https://en.wikipedia.org/wiki/File:Hunger_Games_Film_Poster.jpg",
						"https://www.youtube.com/watch?v=nvU1MnB_dAc")

#print toy_story.storyline
#print avatar.storyline

#avatar.show_trailer()
#armageddon.show_trailer()
movies = [toy_story, avatar, armageddon, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
print media.Movie.valid_ratings