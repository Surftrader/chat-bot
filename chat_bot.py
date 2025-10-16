import random

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


def show_list(items):
    for i, it in enumerate(items, start=1):
        print(f"{i}. {it}")


def recommend_movies():
    print("\nДоступні жанри:", ", ".join(MOVIES.keys()))
    genre = input("Введи жанр: ").strip().lower()
    items = MOVIES.get(genre)
    if not items:
        print("Жанр не знайдено.")
        return
    print(f"\nРекомендації фільмів у жанрі {genre}")
    show_list(items)


def recommend_music():
    print("\nДоступні жанри:", ", ".join(MUSIC.keys()))
    genre = input("Введи жанр: ").strip().lower()
    items = MUSIC.get(genre)
    if not items:
        print("Жанр не знайдено.")
        return
    print(f"\nРекомендації музики у жанрі {genre}")
    show_list(items)


def recommend_games():
    print("\nДоступні жанри:", ", ".join(GAMES.keys()))
    genre = input("Введи жанр: ").strip().lower()
    items = GAMES.get(genre)
    if not items:
        print("Жанр не знайдено.")
        return
    print(f"\nРекомендації ігор у жанрі {genre}")
    show_list(items)


def recommend_menu():
    while True:
        print("\n--- Рекомендації ---")
        print("1. Фільми за жанрами")
        print("2. Музика за жанрами")
        print("3. Ігри за жанрами")
        print("0. Назад")

        choice = input("Вибір: ").strip()

        match choice:
            case "1": recommend_movies()
            case "2": recommend_music()
            case "3": recommend_games()
            case "0":
                break
            case _: print("Невірний вибір, спробуй ще раз.")


def jokester():
    pass


def story_teller():
    pass


def rps_game():
    pass


def guess_number():
    count = 1
    origin_number = random.randint(1, 10)
    while True:
        try:
            print("\nСпробуй вгадати число!")
            number = int(input("Введіть число від 1 до 10: ").strip())
            if number == origin_number:
                print(f"\nТи виграв з {count} спроби!")
                break
            count += 1
            print("\nТи не вгадав. Спробуй ще раз.")
        except Exception as e:
            print("Помилка введення числа. Спробуй ще.")


def games_menu():
    while True:
        print("\n---Ігри---")
        print("1. Камінь-ножниці-папір")
        print("2. Вгадай число")
        print("0. Назад")

        choice = input("Ваш вибір: ").strip()

        match choice:
            case "1": rps_game()
            case "2": guess_number()
            case "0": break
            case _: print("Невірний вибір")


def main_menu():
    while True:
        print("\n===== ГОЛОВНЕ МЕНЮ =====")
        print("1. Рекомендації (фільм / музика / ігри)")
        print("2. Анекдот")
        print("3. Цікава історія")
        print("4. Ігри")
        print("0. Вийти")

        choice = input("Ваш вибір: ").strip()

        match choice:
            case "1": recommend_menu()
            case "2": jokester()
            case "3": story_teller()
            case "4": games_menu()
            case "0":
                print("До зустрічі!")
                break
            case _: print("Невірний вибір, спробуй ще раз.")


def main():
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nВихід...")


if __name__ == '__main__':
    main()
