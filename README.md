# Georgian Spell Correction

A probabilistic Georgian spell checker that suggests the most likely correction for misspelled words using a frequency-based approach.

## Features
- Uses a frequency-based approach to determine the most probable correction.
- Supports one and two-edit distance corrections.
- Efficient implementation using precomputed word frequencies.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/alexnat009/georgian-spell-correction.git
   ```
2. Install dependencies:
   ```sh
   pip install numpy regex
   ```
3. Download the word frequency dataset from [Frequency_Dictionary_GE_363_202](https://github.com/irakli97/Frequency_Dictionary_GE_363_202/tree/master) and place it in the `dataset/` directory.

## Usage
```python
from spell_checker import correction

word = "სწვავე"
print(correction(word))  # Outputs the most likely correction
```

## Citation
This project uses word frequency data from:

> Irakli97. *Frequency Dictionary GE 363 202*. GitHub, 2019. [GitHub Repository](https://github.com/irakli97/Frequency_Dictionary_GE_363_202/tree/master).
