import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://zh.wikipedia.org/wiki/%E7%8E%A9%E5%85%B7%E6%80%BB%E5%8A%A8%E5%91%98#/media/File:Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")
#print(toy_story.storyline)
avatar =  media.Movie("Avatar",
                      "A marine on an alien planet",
                      "https://zh.wikipedia.org/wiki/%E9%98%BF%E5%87%A1%E8%BE%BE#/media/File:Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://en.wikipedia.org/wiki/School_of_Rock#/media/File:School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")
hunger_games = media.Movie("Hunger Games", "A reallly real reality show",
                           "https://en.wikipedia.org/wiki/The_Hunger_Games#/media/File:The_Hunger_Games_cover.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")
Mission_Impossible6 = media.Movie("Mission Impossible: Fallout",
                        "A story of IMF members that are trying to save the world out of the nuclear explosion.",
                        "https://en.wikipedia.org/wiki/Mission:_Impossible_%E2%80%93_Fallout/media/File:MI_%E2%80%93_Fallout.jpg",
                        "https://www.youtube.com/watch?v=XiHiW4N7-bo")
print(Mission_Impossible6.storyline)
Mission_Impossible6.show_trailer()

movies = [toy_story, avatar, school_of_rock, hunger_games]
                             
