import random
import string

class PasswordGenerator:
    def __init__(self):
        pass

    def generate_password(self, length=8, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
        chars = ''
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_special_chars:
            chars += string.punctuation

        if not chars:
            print("Nie wybrano żadnych znaków do generowania hasła.")
            return None

        password = ''.join(random.choice(chars) for _ in range(length))
        return password

if __name__ == "__main__":
    generator = PasswordGenerator()
    length = int(input("Podaj długość hasła: "))
    use_uppercase = input("Czy używać wielkich liter? (t/n): ").lower() == 't'
    use_lowercase = input("Czy używać małych liter? (t/n): ").lower() == 't'
    use_digits = input("Czy używać cyfr? (t/n): ").lower() == 't'
    use_special_chars = input("Czy używać znaków specjalnych? (t/n): ").lower() == 't'

    password = generator.generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
    if password:
        print("Wygenerowane hasło:", password)
        