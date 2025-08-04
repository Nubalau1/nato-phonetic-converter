# NATO Phonetic Alphabet Converter

This is a simple Python script that converts any word into its NATO phonetic equivalent (e.g. `HELLO` → `Hotel Echo Lima Lima Oscar`).

## How It Works

- Loads a CSV file with the NATO alphabet
- Prompts the user for a word
- Translates each letter into its NATO phonetic code
- Handles invalid input (e.g. numbers, symbols)

## Technologies

- Python 3
- pandas

## How to Run

1. Make sure you have `pandas` installed:
```bash
pip install pandas
```
2. Run the script:
```bash
python main.py
```
3. Type a word when prompted.

## Example

```bash
Enter a word: chat
['Charlie', 'Hotel', 'Alpha', 'Tango']
