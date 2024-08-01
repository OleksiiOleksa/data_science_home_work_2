import pandas as pd

# 1. Прочитайте файл 2017_jun_final.csv за допомогою методу read_csv
file_path = '/content/2017_jun_final.csv'  # Шлях до файлу у Google Colab
df = pd.read_csv(file_path)

# 2. Прочитайте отриману таблицю, використовуючи метод head
print("Перші рядки таблиці:")
print(df.head())

# 3. Визначте розмір таблиці за допомогою методу shape
print("\nРозмір таблиці:")
print(df.shape)

# 4. Визначте типи всіх стовпців за допомогою dataframe.dtypes
print("\nТипи всіх стовпців:")
print(df.dtypes)

# 5. Порахуйте, яка частка пропусків міститься в кожній колонці
missing_percentage = df.isnull().mean() * 100
print("\nЧастка пропусків у кожній колонці:")
print(missing_percentage)

# 6. Видаліть усі стовпці з пропусками, крім стовпця "Мова програмування"
columns_to_keep = ['Мова програмування']
columns_with_missing = df.columns[df.isnull().any()].tolist()
columns_to_drop = [col for col in columns_with_missing if col != 'Мова програмування']
df = df.drop(columns=columns_to_drop)

# 7. Знову порахуйте, яка частка пропусків міститься в кожній колонці
missing_percentage_after_drop = df.isnull().mean() * 100
print("\nЧастка пропусків після видалення стовпців:")
print(missing_percentage_after_drop)

# 8. Видаліть усі рядки у вихідній таблиці за допомогою методу dropna
df_cleaned = df.dropna()

# 9. Визначте новий розмір таблиці
print("\nНовий розмір таблиці:")
print(df_cleaned.shape)

# 10. Створіть нову таблицю python_data, в якій будуть тільки рядки зі спеціалістами, які вказали мову програмування Python
python_data = df_cleaned[df_cleaned['Мова програмування'] == 'Python']

# 11. Визначте розмір таблиці python_data
print("\nРозмір таблиці python_data:")
print(python_data.shape)

# 12. Групування за стовпчиком "Посада"
# Перевірте наявність стовпчика "Посада"
if 'Посада' in python_data.columns:
    grouped = python_data.groupby('Посада')

    # 13. Аггрегування даних за стовпчиком "Зарплата на місяць"
    salary_agg = grouped['Зарплата на місяць'].agg(['min', 'max'])
    print("\nМінімальна та максимальна зарплата за посадою:")
    print(salary_agg)
else:
    print("Стовпчик 'Посада' відсутній у даних")

# 14. Створіть функцію fill_avg_salary
def fill_avg_salary(x):
    return x.mean()

# 15. Використовуйте її для методу apply та створіть новий стовпчик "avg"
# Перевірте наявність стовпчика "Зарплата на місяць"
if 'Зарплата на місяць' in python_data.columns:
    python_data['avg'] = python_data.groupby('Посада')['Зарплата на місяць'].transform(fill_avg_salary)

    # 16. Описова статистика для нового стовпчика "avg"
    print("\nОписова статистика для нового стовпчика 'avg':")
    print(python_data['avg'].describe())

    # 17. Збережіть отриману таблицю в CSV файл
    output_path = '/content/python_data_h_w_2_2.csv'  # Шлях до збереження файлу в Google Colab
    python_data.to_csv(output_path, index=False)
    print(f"\nФайл збережено за адресою: {output_path}")
else:
    print("Стовпчик 'Зарплата на місяць' відсутній у даних")
