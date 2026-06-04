from datetime import datetime
import os
import random
import string

def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(all_characters) for _ in range(length))

def save_password_to_file(password):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        if not os.path.exists(desktop_path):
            onedrive_path = os.path.join(
                os.path.expanduser("~"), "OneDrive", "Desktop"
            )
            russian_path = os.path.join(
                os.path.expanduser("~"), "Рабочий стол"
            )
            if os.path.exists(onedrive_path):
                desktop_path = onedrive_path
            elif os.path.exists(russian_path):
                desktop_path = russian_path
            else:
                desktop_path = os.path.dirname(os.path.abspath(__file__))

        filename = os.path.join(desktop_path, "passwords.txt")

        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"[{current_time}] Пароль: {password}\n")

        print(f"✅ Пароль успешно сохранён в: {filename}")

    except Exception as e:
        print(f"\n⚠️ ОШИБКА ЗАПИСИ: {e}")

if __name__ == "__main__":
    print("--- Генератор Паролей ---")
    print("Для выхода введите 'q' и нажмите Enter")

    while True:
        user_input = input("\nВведите длину пароля 4-16 символов (или 'q'): ").strip().lower()

        if not user_input:
            print("Вы ничего не ввели! Введите число.")
            continue

        if user_input in ["q", "й", "выход"]:
            print("Программа завершена.")
            input("\nНажмите Enter, чтобы закрыть это окно")
            break

        try:
            user_length = int(user_input)
            
            if user_length < 4:
                print("Пароль слишком короткий! Установлена минимальная длина: 4")
                user_length = 4
                
            elif user_length > 30:
                print("Пароль слишком длинный! Установлена максимальная длина: 30")
                user_length = 30
                
        except ValueError:
            print("Ошибка! Нужно ввести ЧИСЛО или букву 'q'.")
            continue

        new_password = generate_password(user_length)
        print(f"Ваш новый пароль: {new_password}")

        save_password_to_file(new_password)
