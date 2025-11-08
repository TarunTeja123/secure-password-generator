import string
import secrets

def password_generator(length) :
    all_letters = string.ascii_letters
    all_digits = string.digits
    all_symbols = string.punctuation
    all_characters = all_letters + all_digits + all_symbols
    must_characters = [secrets.choice(string.ascii_uppercase),
                      secrets.choice(string.ascii_lowercase),
                      secrets.choice(string.digits),
                      secrets.choice(string.punctuation)]
    remaining_length = length - 4
    remaining_chars = [secrets.choice(all_characters) for i in range(remaining_length)]
    password_list = must_characters + remaining_chars
    shuffled_password_list = []
    while password_list :
        shuffled_password_list.append(password_list.pop(secrets.randbelow(len(password_list))))
    password = "".join(shuffled_password_list)
    return password
    
def password_strength(password) :
    pwd_length = len(password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(ch in string.punctuation for ch in password)
    count = sum([has_upper,has_lower,has_digit,has_symbol])
    if pwd_length >= 12 and count == 4 :
        return "Strong 💪"
    elif pwd_length >= 8 and count >= 3 :
        return "Medium 👍"
    else :
        return "Weak ⚠️"
    
if __name__ == "__main__" :
    try :
        no_of_passwords = int(input("How Many Passwords You Want To Generate :"))
        password_length = int(input("Enter The Password Length :"))
        if password_length < 4 or no_of_passwords <=0 :
            print("Password Length Must Be Greater Than '4' and No of Passwords Must Be Greater Than '0'")
        else :
            print(f"\nGenerated Passwords : {no_of_passwords}")
            print("-" * 40)
            for i in range(no_of_passwords) :
                new_password = password_generator(password_length)
                rating = password_strength(new_password)
                print(f"{new_password} ===> {rating}")
            print("-" * 40)
    except ValueError :
        print("Invalid Input. Enter A Number")
