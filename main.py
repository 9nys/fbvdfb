def copy_file(source_file_path, destination_file_path):
    try:
        with open(source_file_path, 'r', encoding='utf-8') as source_file:
            content = source_file.read()

        with open(destination_file_path, 'w', encoding='utf-8') as destination_file:
            destination_file.write(content)

        print(f"Файл успішно скопійовано з '{source_file_path}' в '{destination_file_path}'.")
    except FileNotFoundError as e:
        print(f"Файл не знайдено: {e.filename}")
    except Exception as e:
        print(f"Виникла помилка: {e}")


source_file_path = input("Введіть шлях до джерела: ")
destination_file_path = input("Введіть шлях до призначення: ")

copy_file(source_file_path, destination_file_path)
