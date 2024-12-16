import csv
import time
import hashlib
# Ścieżka do pliku
file_path = 'prefix.csv'
country_nr = '48'
salt = '734928293871348791'

# Lista na przedrostki
prefixes = []
prefixes_length_3 = []
prefixes_length_4 = []
prefixes_length_5 = []

# Odczyt pliku CSV
with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row:  # Upewnij się, że wiersz nie jest pusty
            prefix = row[0]
            if len(prefix) == 3:
                prefixes_length_3.append(prefix)
            elif len(prefix) == 4:
                prefixes_length_4.append(prefix)
            elif len(prefix) == 5:
                prefixes_length_5.append(prefix)

# Usuń duplikaty i posortuj
prefixes_length_3 = sorted(set(prefixes_length_3))
prefixes_length_4 = sorted(set(prefixes_length_4))
prefixes_length_5 = sorted(set(prefixes_length_5))

# Wyświetl wyniki
print("Przedrostki o długości 3:", prefixes_length_3)
print("Przedrostki o długości 4:", prefixes_length_4)
print("Przedrostki o dlugosci 5:", prefixes_length_5)
print("Łącznie przedrostków:", len(prefixes_length_5) + len(prefixes_length_3) + len(prefixes_length_4))

# Generowanie numerów telefonów dla przedrostków o długości 3
all_possible_numbers = []
batch_possible_numbers = []
# Przechowywanie hashy dla numerów telefonów
phone_number_hashes = {}
output_file = 'phone_number_hashes.txt'
batch_size = 1000

start_time = time.time()

# def generate_numbers_for_prefix(prefix, length, max_digits):
#     for rest in range(0, 10**max_digits):
#         yield f"{prefix}{rest:0{length}d}"

# Funkcja generująca hashe dla paczki numerów
def generate_hashes(numbers_batch):
    hashes = []
    for number in numbers_batch:
        hashed_number = hashlib.sha256(number.encode()).hexdigest()
        hashes.append(f"{number},{hashed_number}")
    return hashes

# Funkcja zapisująca całą paczkę hashy do pliku
def write_hashes_to_file(hashes_batch, file_path):
    with open(file_path, mode='a', encoding='utf-8') as file:  # Tryb 'a' - dopisywanie
        file.write("\n".join(hashes_batch) + "\n")


# Długość pełnego numeru telefonu w Polsce to 9 cyfr
# Generowanie numerów dla długości przedrostka równego 3
for prefix in prefixes_length_5:
    for i in range(0, 10000, batch_size): # Zakres od 0 do 999999 (6 cyfr)
        for rest in range(i, i+batch_size):
            batch_possible_numbers.append(f"{country_nr}{prefix}{rest:06d}")  # Dodaj wypełnienie zerami\
            # Generowanie hashy dla bieżącej paczki
            hashes_batch = generate_hashes(batch_possible_numbers)

            # Zapis całej paczki do tego samego pliku
            write_hashes_to_file(hashes_batch, output_file)
            batch_possible_numbers = []
            hashes_batch = []
        print(f"Wygenerowana paczka dla i = {i}")


# # Generowanie numerów dla długości przedrostka równego 4
# for prefix in prefixes_length_4:
#     for rest in range(0, 100000):  # Zakres od 0 do 99999 (5 cyfr)
#         all_possible_numbers.append(f"{prefix}{rest:05d}")  # Dodaj wypełnienie zerami
#
# # Generowanie numerów dla długości przedrostka równego 5
# for prefix in prefixes_length_5:
#     for rest in range(0, 10000):  # Zakres od 0 do 9999 (6 cyfr)
#         all_possible_numbers.append(f"{prefix}{rest:04d}")  # Dodaj wypełnienie zerami

end_time = time.time()
elapsed_time = end_time - start_time

# # Przykładowe wyświetlenie części wygenerowanych numerów
# print("Przykładowe wygenerowane numery:")
# print(all_possible_numbers[:10])  # Wyświetl pierwsze 10 numerów
#
# Wyświetl czas generowania
print(f"Czas generowania numerów: {elapsed_time:.2f} sekundy")
# print(f"Łączna ilość wygenerowanych numerów:", len(all_possible_numbers))




# Generowanie i zapisywanie hashy paczkami
# for i in range(0, len(all_possible_numbers)-80000000, batch_size):
#     current_batch = all_possible_numbers[i:i + batch_size]
#     print(f"Przetwarzanie paczki: od {i} do {i + len(current_batch)} numerów...")
#
#     # Generowanie hashy dla bieżącej paczki
#     hashes_batch = generate_hashes(current_batch)
#
#     # Zapis całej paczki do tego samego pliku
#     write_hashes_to_file(hashes_batch, output_file)


# # Rozpocznij generowanie hashy
# for i in range(0, len(all_possible_numbers), batch_size)
# for number in all_possible_numbers:
#     # Oblicz hash SHA-256 dla numeru telefonu
#     # hashed_number = hashlib.sha256(number.encode()).hexdigest()
#     hashed_number = hashlib.md5(number.encode()).hexdigest()
#     # Dodaj numer i jego hash do słownika
#     phone_number_hashes[number] = hashed_number
#


# end_time_2 = time.time()
# elapsed_time_2 = end_time_2 - end_time
# print(f"Czas generowania hashy numerów: {elapsed_time_2:.2f} sekundy")
# Przykładowe wyświetlenie części wyników
# print("Przykładowe hashe numerów:")
# for num, hsh in list(phone_number_hashes.items())[:2]:  # Wyświetl pierwsze 2
#     print(f"Numer: {num}, Hash: {hsh}")

