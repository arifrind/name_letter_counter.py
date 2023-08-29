def main():
    name = input("Please enter your name: ")
    
    # Count the occurrences of each letter in the name
    letter_counts = count_letters(name)
    
    # Display the letter counts
    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")

def count_letters(input_string):
    # Initialize a dictionary to store letter counts
    letter_counts = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            char_lower = char.lower()  # Convert to lowercase
            if char_lower in letter_counts:
                letter_counts[char_lower] += 1
            else:
                letter_counts[char_lower] = 1
            
    return letter_counts

if __name__ == "__main__":
    main()
