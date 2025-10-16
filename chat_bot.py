
def recommend_menu():
    pass


def jokester():
    pass


def story_teller():
    pass


def rps_game():
    pass


def guess_number():
    pass


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
