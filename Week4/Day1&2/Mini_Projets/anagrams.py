
#Suite mini projet 

from anagram_checker import AnagramChecker

def clean_input(word):
    return word.strip()

def is_valid_input(word):
    return word.isalpha() and " " not in word

def main():
    checker = AnagramChecker()

    while True:
        print("\n--- ANAGRAM CHECKER ---")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '2':
            print("Goodbye!")
            break
        elif choice == '1':
            user_input = input("Enter a word: ")
            word = clean_input(user_input)

            if not is_valid_input(word):
                print("❌ Invalid input. Please enter a single alphabetic word.")
                continue

            if not checker.is_valid_word(word):
                print(f"❌ '{word}' is not a valid English word.")
                continue

            anagrams = checker.get_anagrams(word)

            print("\n🎉 Result:")
            print(f"YOUR WORD : \"{word.upper()}\"")
            print("This is a valid English word.")
            print(f"Anagrams for your word: {', '.join(anagrams)}")
        else:
            print("❌ Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
