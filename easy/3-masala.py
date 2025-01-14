from colorama import Fore, Style

class Movie:
    def __init__(self, title, duration, rating):
        self.title = title
        self.duration = duration
        self.rating = rating

    def increase_duration(self, minutes):
        self.duration += minutes
        
        if self.duration > 150:
            self.rating -= 0.5

movie = Movie("Puling bo'lsa", 1100, 5.0)
print(f"{Fore.GREEN} {Style.BRIGHT}---film nomi: {movie.title}, davomiyligi: {movie.duration} minut, reyting: {movie.rating}")

movie.increase_duration(50)
print(f"{Fore.GREEN } {Style.BRIGHT} {Style.DIM}---davomiylik: {movie.duration} minut, yangi reyting: {movie.rating}")
