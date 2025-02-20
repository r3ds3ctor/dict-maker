import itertools
import argparse
from tqdm import tqdm

def calculate_number_of_permutations(word, special_chars, digits, add_to_start, add_to_end):
    base_permutations = 2 ** len(word)  # Each letter can be uppercase or lowercase

    # Generate special character combinations (1 to 2 max)
    special_combinations = [''] + list(special_chars) + [''.join(comb) for comb in itertools.combinations_with_replacement(special_chars, 2)]
    
    # Generate all digit combinations (1 to 4 digits)
    digit_permutations = [str(i) for i in range(10)]  # Single digits (0-9)
    digit_permutations += [str(i).zfill(2) for i in range(10, 100)]  # Two-digit numbers (00-99)
    digit_permutations += [str(i).zfill(3) for i in range(100, 1000)]  # Three-digit numbers (000-999)
    digit_permutations += [str(i) for i in range(1000, 10000)]  # Four-digit numbers (0000-9999)

    # Generate full permutations of numbers + special characters
    combined_suffixes = digit_permutations + [d + s for d in digit_permutations for s in special_combinations]

    start_combinations = len(combined_suffixes) if add_to_start else 1
    end_combinations = len(combined_suffixes) if add_to_end else 1

    return base_permutations * start_combinations * end_combinations

def generate_permutations(word, special_chars, digits, add_to_start, add_to_end, output_file):
    base_word_combinations = {''.join(comb) for comb in itertools.product(*[(c.lower(), c.upper()) for c in word])}

    # Generate special character combinations (1 to 2 max)
    special_combinations = [''] + list(special_chars) + [''.join(comb) for comb in itertools.combinations_with_replacement(special_chars, 2)]

    # Generate all digit combinations (1 to 4 digits)
    digit_permutations = [str(i) for i in range(10)]  # Single digits (0-9)
    digit_permutations += [str(i).zfill(2) for i in range(10, 100)]  # Two-digit numbers (00-99)
    digit_permutations += [str(i).zfill(3) for i in range(100, 1000)]  # Three-digit numbers (000-999)
    digit_permutations += [str(i) for i in range(1000, 10000)]  # Four-digit numbers (0000-9999)

    # Generate full permutations of numbers + special characters
    combined_suffixes = digit_permutations + [d + s for d in digit_permutations for s in special_combinations]

    with open(output_file, "w") as file:
        total_permutations = calculate_number_of_permutations(word, special_chars, digits, add_to_start, add_to_end)
        with tqdm(total=total_permutations, desc="Generating dictionary", unit="perm") as pbar:
            for base_word in base_word_combinations:
                if add_to_start:
                    for prefix in combined_suffixes:
                        new_word_start = prefix + base_word
                        if add_to_end:
                            for suffix in combined_suffixes:
                                file.write(new_word_start + suffix + "\n")
                                pbar.update(1)
                        else:
                            file.write(new_word_start + "\n")
                            pbar.update(1)
                else:
                    if add_to_end:
                        for suffix in combined_suffixes:
                            file.write(base_word + suffix + "\n")
                            pbar.update(1)
                    else:
                        file.write(base_word + "\n")
                        pbar.update(1)

def main():
    parser = argparse.ArgumentParser(
        description="Generate a dictionary with controlled permutations of a given word, including uppercase/lowercase variations and special characters/digits at the start or end.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument("word", type=str, help="The base word for generating permutations.")
    parser.add_argument("-s", "--special", type=str, default="#$%/.!", 
                        help='Special characters to include (max 2). Default: "#$%/.!"')
    parser.add_argument("-d", "--digits", type=str, default="0123456789", 
                        help="Digits to include (max 4). Default: \"0123456789\"")
    parser.add_argument("--start", action="store_true", help="Add special characters/digits at the beginning of the word.")
    parser.add_argument("--end", action="store_true", help="Add special characters/digits at the end of the word.")
    parser.add_argument("-o", "--output", type=str, default="dictionary.txt", help="Output file name (default: dictionary.txt).")
    
    args = parser.parse_args()

    word = args.word
    special_chars = args.special
    digits = args.digits
    add_to_start = args.start
    add_to_end = args.end
    output_file = args.output

    num_permutations = calculate_number_of_permutations(word, special_chars, digits, add_to_start, add_to_end)
    file_size = num_permutations * (len(word) + 6 + 1)  # +6 for max prefix/suffix, +1 newline

    print(f"Number of possible permutations: {num_permutations}")
    print(f"Estimated file size: {file_size / (1024 ** 2):.2f} MB")

    confirmation = input("Do you want to continue with the dictionary generation? (y/n): ")
    if confirmation.lower() == 'y':
        generate_permutations(word, special_chars, digits, add_to_start, add_to_end, output_file)
        print(f"Dictionary generated and saved in '{output_file}'")
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    main()
