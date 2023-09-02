import sys
import string
from scapy.all import rdpcap

# Función para descifrar un mensaje utilizando el corrimiento especificado
def decrypt_message(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

# Función para calcular la frecuencia de aparición de letras en un mensaje
def calculate_letter_frequencies(message):
    letter_freq = {}
    total_letters = 0

    for char in message:
        if char.isalpha():
            letter_freq[char] = letter_freq.get(char, 0) + 1
            total_letters += 1

    # Calcula las frecuencias relativas
    for char, freq in letter_freq.items():
        letter_freq[char] = freq / total_letters

    return letter_freq

# Función para imprimir el mensaje con el corrimiento más probable
def print_best_guess(message, letter_freq_esp):
    best_shift = None
    best_score = float('-inf')
    best_decryption = ""
    all_messages = []
    
    for shift in range(26):
        decrypted_message = decrypt_message(message, shift)
        letter_freq = calculate_letter_frequencies(decrypted_message)
        all_messages.append(str(shift) + "\t" + decrypted_message)

        # Calcula la puntuación comparando las frecuencias con el español
        score = sum(letter_freq_esp[char] * letter_freq.get(char, 0) for char in letter_freq_esp)

        if score > best_score:
            best_score = score
            best_shift = shift
            best_decryption = decrypted_message

    all_messages[best_shift] = str(best_shift) + "\t" + "\033[92m" + best_decryption + "\033[0m"
    # Imprime el mejor intento en verde
    for string in all_messages:
        print(string)

if len(sys.argv) != 2:
    print("Uso: python decrypt.py captura.pcapng")
    sys.exit(1)

file_name = sys.argv[1]

try:
    packets = rdpcap(file_name)
except FileNotFoundError:
    print("El archivo especificado no existe.")
    sys.exit(1)

# Frecuencias de letras en español
letter_freq_esp = {
    'a': 0.1253,
    'b': 0.0142,
    'c': 0.0463,
    'd': 0.0583,
    'e': 0.1368,
    'f': 0.0069,
    'g': 0.0101,
    'h': 0.0070,
    'i': 0.0625,
    'j': 0.0044,
    'k': 0.0002,
    'l': 0.0497,
    'm': 0.0315,
    'n': 0.0671,
    'o': 0.0868,
    'p': 0.0251,
    'q': 0.0088,
    'r': 0.0687,
    's': 0.0798,
    't': 0.0463,
    'u': 0.0393,
    'v': 0.0090,
    'w': 0.0001,
    'x': 0.0022,
    'y': 0.0090,
    'z': 0.0052,
}

decrypted_message = ""

for packet in packets:
    if packet.haslayer("ICMP"):
        icmp_data = bytes(packet["ICMP"].payload)[-48:]  # Obtén los últimos 48 bytes
        first_char = chr(icmp_data[0])  # Obtén el primer byte como carácter
        decrypted_message += first_char

print("Mensaje cifrado obtenido:", decrypted_message)
print("Intentos de descifrado:")

print_best_guess(decrypted_message, letter_freq_esp)
