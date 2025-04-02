# 📅 df-datefixer

**A simple yet powerful Python package to automatically standardize and fix dates in Pandas DataFrames.**

---

## 🌟 Overview

`df-datefixer` effortlessly handles messy date columns in your DataFrames by automatically:
- Detecting and parsing dates in multiple formats.
- Converting them into your preferred standardized date format.
- Managing invalid or missing dates by replacing them with a custom placeholder.
- Providing clear, informative feedback on any problematic entries.

Ideal for data scientists who regularly encounter inconsistent date formats during preprocessing.

---

## 🚀 Quick Installation

Install quickly via pip:

```shell
pip install df-datefixer
```

---

## ✨ How to Use

Here's a simple example:

```python
import pandas as pd
from df_datefixer.fixer import fix_dates

# create your messy DataFrame
df = pd.DataFrame({
    'event_date': ['2022-01-01', '1/2/2022', '03-01-2022', 'not a date', None]
})

# standardize your dates easily
df_clean = fix_dates(df, column="event_date", target_format="%Y-%m-%d", missing_value="0")

print(df_clean)
```

### 🖥️ Output:

```
⚠️ 2 problematic date values found in column 'event_date':
- Row 3: not a date
- Row 4: None (missing)

  event_date
0  2022-01-01
1  2022-01-02
2  2022-03-01
3           0
4           0
```

---

## ⚙️ Parameters

- **`df`** *(pd.DataFrame)*: Your Pandas DataFrame.
- **`column`** *(str)*: Column containing date values to fix.
- **`target_format`** *(str)*: Desired output date format (default: `%Y-%m-%d`).
- **`missing_value`** *(str)*: Placeholder for missing/unparsable dates (default: `"0"`).
- **`verbose`** *(bool)*: Whether to print issues found (default: `True`).

---

## 🛠️ Dependencies

- pandas
- python-dateutil

Dependencies will be automatically installed upon running `pip install df-datefixer`.

---

## 🧪 Running Tests

Clone the repository and install in editable mode:

```shell
git clone https://github.com/kyriaki-mvr/df-datefixer.git
cd df-datefixer
pip install -e .
pip install pytest
pytest tests
```

---

## 💡 Contributions

Feel free to submit pull requests, suggest improvements, or report issues on GitHub. Your contribution makes the package better for everyone!

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

🎉 Enjoy easily fixing dates in your Pandas DataFrames!
