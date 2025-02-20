# dict-maker

A Python tool to generate custom dictionaries with controlled permutations of a base word, including uppercase/lowercase variations, special characters, and digits at the beginning or end.

## Usage

### Requirements
- Python 3.x
- Libraries: `argparse`, `itertools`, `tqdm` (install via `pip install tqdm`).

### Installation
Clone the repository and run the script:
```bash
git clone https://github.com/yourusername/dict-maker.git
cd dict-maker
```
### Execution
Run the script with the following arguments:

```bash
python dict_maker.py <base_word> [options]
```
Options
-s or --special: Special characters to include (default: #$%/.!).

-d or --digits: Digits to include (default: 0123456789).

--start: Add special characters/digits at the beginning of the word.

--end: Add special characters/digits at the end of the word.

-o or --output: Output file name (default: dictionary.txt).

### Example
```bash
python dict_maker.py password --start --end -s "@#" -d "123" -o custom_dict.txt
```
### Output
When running the script, a progress bar will be displayed using tqdm, and a text file with the permutations will be generated.
<img width="738" alt="Screenshot 2025-02-20 at 11 46 25 AM" src="https://github.com/user-attachments/assets/fb45fe52-6cde-4188-8517-a9364724abfe" />

### License
This project is licensed under the MIT License.

Developed by Alexander B.

### Collaboration
Contributions are welcome! If you'd like to improve the code, report an issue, or suggest a new feature, follow these steps:

1. Fork the repository.
2. Create a branch for your contribution (git checkout -b feature/new-feature).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push your changes to your fork (git push origin feature/new-feature).
5. Open a Pull Request in the original repository.

## 🤝 Contributing
Contributions, feedback, and improvements are always welcome!  
If you find this tool useful and would like to support its development, you can do so here:  
👉 (buymeacoffee.com/alexboteroh)






