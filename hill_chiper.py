import numpy as np

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def get_matrix_inverse(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det, 26)

    if det_inv is None:
        raise ValueError("Determinan tidak memiliki invers modular 26, matriks tidak dapat didekripsi.")

    adjugate = np.array([[matrix[1, 1], -matrix[0, 1]],
                         [-matrix[1, 0], matrix[0, 0]]])

    inv_matrix = (det_inv * adjugate) % 26
    return inv_matrix

def text_to_matrix(text):
    text = ''.join(filter(str.isalpha, text)).upper()
    if len(text) % 2 != 0:
        text += 'X'

    numbers = [ord(char) - ord('A') for char in text]
    matrix = np.array(numbers).reshape(-1, 2).T
    return matrix

def matrix_to_text(matrix):
    numbers = matrix.T.flatten()
    text = ''.join([chr(num + ord('A')) for num in numbers])
    return text

def encrypt():
    try:
        plaintext = input("Masukkan plaintext: ")
        key_str = input("Masukkan kunci matriks 2x2 (4 angka dipisah spasi, cth: 7 6 2 5): ")
        
        key_nums = list(map(int, key_str.split()))
        if len(key_nums) != 4:
            print("\n[Error] Kunci harus terdiri dari 4 angka.")
            return

        key_matrix = np.array(key_nums).reshape(2, 2)
        
        det = int(np.round(np.linalg.det(key_matrix)))
        if mod_inverse(det, 26) is None:
            print("\n[Error] Determinan dari matriks kunci ini tidak valid (tidak koprima dengan 26). Coba kunci lain.")
            return

        plain_matrix = text_to_matrix(plaintext)
        
        cipher_matrix = (key_matrix @ plain_matrix) % 26
        
        ciphertext = matrix_to_text(cipher_matrix)
        
        print(f"\nPlaintext Asli : {plaintext}")
        print(f"Kunci Matriks    :\n{key_matrix}")
        print(f"Ciphertext Hasil : {ciphertext}")

    except Exception as e:
        print(f"\n[Error] Terjadi kesalahan: {e}")

def decrypt():
    try:
        ciphertext = input("Masukkan ciphertext: ")
        key_str = input("Masukkan kunci matriks 2x2 (4 angka dipisah spasi, cth: 7 6 2 5): ")
        
        key_nums = list(map(int, key_str.split()))
        if len(key_nums) != 4:
            print("\n[Error] Kunci harus terdiri dari 4 angka.")
            return

        key_matrix = np.array(key_nums).reshape(2, 2)
        
        inv_key_matrix = get_matrix_inverse(key_matrix)
        
        cipher_matrix = text_to_matrix(ciphertext)
        
        plain_matrix = (inv_key_matrix @ cipher_matrix) % 26
        
        plaintext = matrix_to_text(plain_matrix)
        
        print(f"\nCiphertext Asli  : {ciphertext}")
        print(f"Kunci Matriks      :\n{key_matrix}")
        print(f"Invers Kunci       :\n{inv_key_matrix}")
        print(f"Plaintext Hasil  : {plaintext}")

    except ValueError as e:
        print(f"\n[Error] {e}")
    except Exception as e:
        print(f"\n[Error] Terjadi kesalahan saat dekripsi: {e}")

def find_key():
    try:
        known_plain = input("Masukkan 4 karakter plaintext yang diketahui (cth: PYTH): ")
        known_cipher = input("Masukkan 4 karakter ciphertext yang bersesuaian (cth: PUTV): ")

        if len(known_plain) != 4 or len(known_cipher) != 4 or not known_plain.isalpha() or not known_cipher.isalpha():
            print("\n[Error] Input harus berupa 4 karakter alfabet.")
            return
            
        P = text_to_matrix(known_plain)
        C = text_to_matrix(known_cipher)
        
        P_inv = get_matrix_inverse(P)
        
        key_matrix = (C @ P_inv) % 26
        
        print("\nPlaintext Matrix (P):\n", P)
        print("Ciphertext Matrix (C):\n", C)
        print("Invers Plaintext Matrix (P^-1):\n", P_inv)
        print("\nMatriks Kunci yang Ditemukan (K):\n", key_matrix)

    except ValueError as e:
        print(f"\n[Error] {e}")
    except Exception as e:
        print(f"\n[Error] Terjadi kesalahan saat mencari kunci: {e}")

def main():
    while True:
        print("\n--- Program Hill Cipher ---")
        print("1. Enkripsi Teks")
        print("2. Dekripsi Teks")
        print("3. Cari Kunci (Known Plaintext)")
        print("4. Keluar")
        choice = input("Pilih operasi (1/2/3/4): ")

        if choice == '1':
            encrypt()
        elif choice == '2':
            decrypt()
        elif choice == '3':
            find_key()
        elif choice == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
