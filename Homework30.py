class MyShows:
    def __init__(self, name, platform, release_year, current_episode=1, rating=None, main_actors=None):
        if not isinstance(name, str) or not isinstance(platform, str):
            raise TypeError("Name and platform must be strings.")
        if not isinstance(release_year, int) or not isinstance(current_episode, int):
            raise TypeError("Release year and current episode must be integers.")
        if rating is not None and (not isinstance(rating, int) or not (1 <= rating <= 10)):
            raise ValueError("Rating must be an integer between 1 and 10.")
        if main_actors is not None and not isinstance(main_actors, list):
            raise TypeError("Main actors must be a list.")

        self.__name = name
        self.__platform = platform
        self.__release_year = release_year
        self.__current_episode = current_episode
        self.__rating = rating
        self.__main_actors = main_actors

    @property
    def name(self):
        return self.__name

    @property
    def platform(self):
        return self.__platform

    @property
    def release_year(self):
        return self.__release_year

    @property
    def current_episode(self):
        return self.__current_episode

    @property
    def rating(self):
        return self.__rating

    @property
    def main_actors(self):
        return self.__main_actors

    @current_episode.setter
    def current_episode(self, episode):
        if not isinstance(episode, int):
            raise TypeError("Current episode must be an integer.")
        if episode < 1:
            raise ValueError("Current episode must be at least 1.")
        self.__current_episode = episode

    @rating.setter
    def rating(self, new_rating):
        if not isinstance(new_rating, int) or not (1 <= new_rating <= 10):
            raise ValueError("Rating must be an integer between 1 and 10.")
        self.__rating = new_rating

    @rating.deleter
    def rating(self):
        self.__rating = None

    def get_info(self):
        info = f"Name: {self.__name}\nPlatform: {self.__platform}\nRelease Year: {self.__release_year}\n"
        info += f"Current Episode: {self.__current_episode}\nRating: {self.__rating}\n"
        info += f"Main Actors: {self.__main_actors if self.__main_actors else 'None'}"
        return info