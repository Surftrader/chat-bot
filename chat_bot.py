import random

try:
    from prettytable import PrettyTable
except Exception:
    PrettyTable = None

try:
    from art import tprint
except Exception:
    tprint = None

try:
    import pyjokes
except Exception:
    pyjokes = None

try:
    import emoji as emoji_pkg
except Exception:
    emoji_pkg = None

try:
    from colorama import Fore, Back, Style, init as colorama_init
    colorama_init()
except Exception:
    Fore = Back = Stryle = None


MOVIES = {
    "комедія": ["The Grand Budapest Hotel", "Groundhog Day", "Superbad", "Кавказька полонянка (укр.)"],
    "драма": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "фантастика": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "анімація": ["Spirited Away", "Toy Story", "Coco"]
}

MUSIC = {
    "рок": ["Queen - Bohemian Rhapsody", "Nirvana - Smells Like Teen Spirit", "The Beatles - Hey Jude"],
    "поп": ["Dua Lipa - Levitating", "Taylor Swift - Shake It Off", "Michael Jackson - Billie Jean"],
    "джаз": ["Miles Davis - So What", "John Coltrane - Naima"],
    "класика": ["Beethoven - Symphony No.5", "Mozart - Eine kleine Nachtmusik"]
}

GAMES = {
    "логічні": ["Sudoku", "Chess", "2048"],
    "мультіплеєр": ["Among Us", "League of Legends", "Dota 2"],
    "аркади": ["Tetris", "Super Mario Bros", "Geometry Dash"]
}

JOKES = [
    "— Слон у слона зайняв місце в бібліотеці — що він читав? — Тренінг пам’яті.",
    "— Який найкоротший шлях до серця програміста? — через Git push.",
]

STORIES = [
    "Колись давно один студент написав програму, яка замість звіту надрукувала 'Вітаю, світ!'. Всі отримали A.",
    "Був собі робот, який мріяв стати поетом. Він почав з генерації рим на основі логів — і вийшло феєрично."
]


def _c(text: str, color: str = None):
    if Fore and Style and color:
        col = getattr(Fore, color.upper(), "")
        return f"{col}{text}{Style.RESET_ALL}"
    return text


def show_list(items):
    if PrettyTable:
        table = PrettyTable()
        table.field_names = ["№", "Назва"]
        for i, it in enumerate(items, start=1):
            table.add_row([i, it])
        print(table)
    else:
        for i, it in enumerate(items, start=1):
            print(f"{i}. {it}")


def ask_genre(genres, recommendation):
    print(_c("\nДоступні жанри:", "YELLOW"), ", ".join(genres.keys()))
    genre = input("Введи жанр: ").strip().lower()
    items = genres.get(genre)
    if not items:
        print(_c("Жанр не знайдено.", "RED"))
        return
    print(_c(f"\n{recommendation} {genre}", "MAGENTA"))
    show_list(items)


def recommend_movies():
    ask_genre(MOVIES, "\nРекомендації фільмів у жанрі")


def recommend_music():
    ask_genre(MUSIC, "\nРекомендації музики у жанрі")


def recommend_games():
    ask_genre(GAMES, "\nРекомендації ігор у жанрі")


def recommend_menu():
    while True:
        print(_c("\n--- Рекомендації ---", "BLUE"))
        print("1. Фільми за жанрами")
        print("2. Музика за жанрами")
        print("3. Ігри за жанрами")
        print(_c("0. Назад", "RED"))

        choice = input("Вибір: ").strip()

        match choice:
            case "1": recommend_movies()
            case "2": recommend_music()
            case "3": recommend_games()
            case "0":
                break
            case _: print(_c("Невірний вибір, спробуй ще раз.", "RED"))


def get_random_choice(prompt, values):
    print(_c(prompt, "BLUE"))
    print(random.choice(values))


def jokester():
    jokes = pyjokes.get_jokes() if pyjokes else JOKES
    get_random_choice("\n--- Анекдот ---", jokes)


def story_teller():
    get_random_choice("\n--- Цікава історія ---", STORIES)


def rps_result(user, comp):
    """0 - нічия, 1 - юзер виграв, 2 - комп виграв"""
    if user == comp:
        return 0
    wins = {("1, 2"), ("2", "3"), ("3", "1")}
    if (user, comp) in wins:
        return 1
    return 2


def rps_game():
    moves = {"1": "Камінь", "2": "Ножиці", "3": "Папір"}

    print(_c("\n=== Камінь-ножиці-папір ===", "BLUE"))
    print("1 - Камінь, 2 - Ножиці, 3 - Папір, 0 - Вихід")

    while True:

        choice = input("Твій хід: ").strip()
        if choice == "0":
            break
        if not choice in moves:
            print(_c("Невірний вибір. Спробуй ще.", "RED"))
            continue
        random_choice = random.choice(list(moves.keys()))

        print(f"Ти: {moves[choice]} VS Комп'ютер: {moves[random_choice]}")
        result = rps_result(choice, random_choice)

        match result:
            case 0: print(_c("Нічия!", "YELLOW"))
            case 1: print(_c("Ти виграв!", "GREEN"))
            case _: print(_c("Ти програв.", "RED"))


def guess_number():
    count = 1
    origin_number = random.randint(1, 10)
    while True:
        try:
            print("\nСпробуй вгадати число!")
            number = int(input("Введіть число від 1 до 10: ").strip())
            if number == origin_number:
                print(_c(f"\nТи виграв з {count} спроби!", "GREEN"))
                break
            count += 1
            print(_c("\nТи не вгадав. Спробуй ще раз.", "RED"))
        except Exception as e:
            print(_c("Помилка введення числа. Спробуй ще.", "RED"))


def games_menu():
    while True:
        print(_c("\n--- Ігри ---", "BLUE"))
        print("1. Камінь-ножниці-папір")
        print("2. Вгадай число")
        print(_c("0. Назад", "RED"))

        choice = input("Ваш вибір: ").strip()

        match choice:
            case "1": rps_game()
            case "2": guess_number()
            case "0": break
            case _: print("Невірний вибір")


def emoji_main_menu():
    print(
        f"{emoji_pkg.emojize("1. :clapper_board: Рекомендації (фільм / музика / ігри)")}")
    print(f"{emoji_pkg.emojize("2. :face_with_tears_of_joy: Анекдот")}")
    print(f"{emoji_pkg.emojize("3. :books: Цікава історія")}")
    print(f"{emoji_pkg.emojize("4. :video_game: Ігри")}")
    print(_c(f"{emoji_pkg.emojize("0. :door: Вийти")}", "RED"))


def simple_main_menu():
    print("1. Рекомендації (фільм / музика / ігри)")
    print("2. Анекдот")
    print("3. Цікава історія")
    print("4. Ігри")
    print(_c("0. Вийти", "RED"))


def main_menu():
    while True:

        print(_c("\n===== ГОЛОВНЕ МЕНЮ =====", "GREEN"))
        emoji_main_menu() if emoji_pkg else simple_main_menu()

        choice = input("Ваш вибір: ").strip()

        match choice:
            case "1": recommend_menu()
            case "2": jokester()
            case "3": story_teller()
            case "4": games_menu()
            case "0":
                print(_c("\nДО ЗУСТРІЧІ!", "YELLOW"))
                break
            case _: print(_c("Невірний вибір, спробуй ще раз.", "RED"))


def banner():
    if tprint:
        tprint("\nENTERTAIN\nBOT", font="small")
    else:
        print("ENTERTAIN\nBOT")


def main():
    banner()
    try:
        main_menu()
    except KeyboardInterrupt:
        print(_c("\nВихід...", "RED"))


if __name__ == '__main__':
    main()
