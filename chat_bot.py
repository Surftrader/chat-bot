import random


def recommend_movies():
    pass


def recommend_music():
    pass


def recommend_games():
    pass


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
