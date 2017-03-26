
import film
import my_fav_movies

Fifty_Shades_Darker = film.Movie("Fifty Shades Darker", 
                                 "Following the events of Fifty Shades of Grey, Anastasia Ana Steele tries to move on from her relationship with Christian Grey."
                                 "A wounded Christian convinces her to resume their romance under Ana's conditions. As the couple begins their normal relationship,"
                                 "Christian's past threatens to tear the couple apart.", 
                                 "https://upload.wikimedia.org/wikipedia/en/2/2d/Fifty_Shades_Darker_film_poster.jpg", 
                                 "https://www.youtube.com/watch?v=n6BVyk7hty8")

#print(Fifty_Shades_Darker.storyline)

The_Fate_of_the_Furious=film.Movie("The Fate of the Furious",
                                   "With Dom and Letty on their honeymoon, Brian and Mia having retired from the game,"
                                   "and the rest of the crew exonerated,the team has found a semblance of a normal life."
                                   "But when a mysterious woman seduces Dom into a world of crime he cannot seem to escape,"
                                   "causing him to betray those closest to him, they will face trials that will test them as never before.",
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/F8_teaser_poster.jpg/220px-F8_teaser_poster.jpg",
                                   "https://www.youtube.com/watch?v=JwMKRevYa_M")
American_Pie_1=film.Movie("American Pie 1",
                          "Five high school seniors from West Michigan are good friends: Jim Levenstein (Jason Biggs)"
                          "an awkward, nerdy and sexually naïve character whose dad Noah (Eugene Levy)"
                          "attempts to offer sexual advice including purchasing and giving him pornography",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/c8/American_Pie1.jpg/220px-American_Pie1.jpg",
                          "https://www.youtube.com/watch?v=iUZ3Yxok6N8")
Need_For_Speed=film.Movie("Need For Speed",
                           "Need for Speed is a 2014 American action film"
                           "Tobey Marshall is a former race car driver who owns a garage named Marshall Motors in Mount Kisco, New York"
                           "where he and his friends tune performance cars."
                           "Struggling to make ends meet, he and his crew participate in street races after hours",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/e/e3/Need_For_Speed_poster.jpg/220px-Need_For_Speed_poster.jpg",
                           "https://www.youtube.com/watch?v=fsrJWUVoXeM")
#print(The_Fate_of_the_Furious.title)
#print(The_Fate_of_the_Furious.storyline)
#sThe_Fate_of_the_Furious.shw_trailer()
movies = [Fifty_Shades_Darker,The_Fate_of_the_Furious,American_Pie_1,Need_For_Speed]
my_fav_movies.open_movies_page(movies)
#print (film.Movie.__module__)
