import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    def __init__(self, title, duration, movie_storyline, poster_image, trailer_youtube):
        super().__init__(title, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Tvshow(Video):
    def __init__(self, title, duration, Tvshow_season, Tvshow_episode, Tv_station):
        super().__init__(title, duration)
        self.season = Tvshow_season
        self.episode = Tvshow_episode
        self.station = Tv_station

    def get_local_listing(self):
        print("Season - "+str(Tvshow_season))
        print("Episode - "+str(Tvshow_episode))

toy_story = Movie("Toy Story", "200mins", "A story of a boy and his toys that come to life",
                     "https://zh.wikipedia.org/wiki/%E7%8E%A9%E5%85%B7%E6%80%BB%E5%8A%A8%E5%91%98#/media/File:Movie_poster_toy_story.jpg",
                  "https://www.youtube.com/watch?v=4KPTXpQehio")

Mission_Impossible = Tvshow("Mission_Impossible1","60mins","1", "1", "Paramounta Television")
print(toy_story.title)
print(toy_story.storyline)
print(Mission_Impossible.station)

