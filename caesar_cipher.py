def encrypt(phrase: str, shift: int):
    result = ""
    for i in phrase:
        if i == " ":
            # if character is a space, add the space
            result += " "
        elif i.islower():
            result += chr((ord(i) - ord("a") + shift) % 26 + ord("a"))
        elif i.isupper():
            result += chr((ord(i) - ord("A") + shift) % 26 + ord("A"))
        else:
            # if the current letter isn't in the alphabet, add it like that
            result += i
    return result


def decrypt(phrase: str, shift: int):
    result = ""
    for i in phrase:
        if i == " ":
            result += " "
        elif i.islower():
            result += chr((ord(i) - ord("a") - shift) % 26 + ord("a"))
        elif i.isupper():
            result += chr((ord(i) - ord("A") - shift) % 26 + ord("A"))
        else:
            result += i
    return result


def main():
    done = False
    while not done:
        choice = input("[E]ncrypt, [D]ecrypt, or [Q]uit: ").lower()
        if choice == "e":
            phrase = input("What is the phrase: ")
            shift = int(input("What is the shift: "))
            print(f"Encrypted: {encrypt(phrase, shift)}")
        elif choice == "d":
            phrase = input("What is the phrase: ")
            a_word = input("What is a word inside the phrase: ")
            for i in range(1, 26):
                decrypted = decrypt(phrase, i)
                if a_word in decrypted:
                    break
            # If the loop doesn't break, then the word is not inside any version of decrypted phrase, and the user is wrong
            else:
                print("Could not decrypt. Your inputted word is not in the decrypted phrase.")
                continue
            print(f"The shift is -> {i}")
            print(f"The full phrase is -> {decrypted}")
        elif choice == "q":
            done = True


if __name__ == "__main__":
    main()
