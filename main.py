import os
import time
import pyautogui


def open_calculator():
    platform = os.name
    try:
        if platform == "nt":
            os.system("start calc")
        elif platform == "posix":
            if os.uname().sysname == "Darwin":
                os.system("open -a Calculator")
            else:
                os.system("gnome-calculator")
        else:
            raise OSError("Неизвестная операционная система")
    except Exception as e:
        print(f"Ошибка при открытии калькулятора: {e}")
        custom_path = input("Введите полный путь до приложения калькулятора: ").strip()
        if os.path.exists(custom_path):
            try:
                os.system(f'"{custom_path}"')
            except Exception as inner_e:
                print(f"Не удалось открыть калькулятор по указанному пути: {inner_e}")
        else:
            print("Указанный путь не существует. Попробуйте снова.")


def press_button(screenshot: str):
    button = pyautogui.locateOnScreen(screenshot, confidence=0.9)
    if button:
        pyautogui.click(pyautogui.center(button))
    else:
        print(f"Не удалось найти {screenshot}. Проверьте скриншот и повторите попытку.")
        raise ValueError(f"Не найдена кнопка {screenshot} на экране")


def perform_calculation():
    time.sleep(1)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    screenshots_dir = os.path.join(base_dir, "screenshots")

    buttons = [
        os.path.join(screenshots_dir, "button_1.png"),
        os.path.join(screenshots_dir, "button_2.png"),
        os.path.join(screenshots_dir, "button_plus.png"),
        os.path.join(screenshots_dir, "button_7.png"),
        os.path.join(screenshots_dir, "button_equal.png"),
    ]

    for button in buttons:
        try:
            press_button(button)
        except ValueError as e:
            print(f"Ошибка при нажатии: {e}")
            return


def main():
    try:
        open_calculator()
        perform_calculation()
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
