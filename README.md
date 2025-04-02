# df-datefixer 📅

[![PyPI](https://img.shields.io/pypi/v/df-datefixer.svg)](https://pypi.org/project/df-datefixer/)
[![License](https://img.shields.io/github/license/your-username/df-datefixer)](LICENSE)

`df-datefixer` is a lightweight Python package to quickly standardize dates in Pandas DataFrames. It seamlessly handles inconsistent date formats and automatically manages missing or invalid entries.

---

## 🚀 Installation

```shell
pip install df-datefixer
```

---

## 📖 Usage

```python
import pandas as pd
from df_datefixer.fixer import fix_dates

df = pd.DataFrame({
    'event_date': ['2022-01-01', '1/2/2022', 'bad-date', None]
})

fixed_df = fix_dates(df, column="event_date", target_format="%Y-%m-%d", missing_value="0")

print(fixed_df)
```

**Output:**

```
⚠️ 2 problematic date values found in column 'event_date':
- Row 2: bad-date
- Row 3: None (missing)

  event_date
0  2022-01-01
1  2022-01-02
2           0
3           0
```

---

## ⚙️ Parameters

- `df`: Input Pandas DataFrame.
- `column`: Name of column containing dates.
- `target_format`: Desired standardized date format (default: `%Y-%m-%d`).
- `missing_value`: Replacement for missing/unparsable dates (default: `'0'`).
- `verbose`: Print details about problematic dates (default: `True`).

---

## 🧑‍💻 Development and Tests

Clone and install in editable mode for local development:

```shell
git clone https://github.com/kyriaki-mvr/df-datefixer.git
cd df-datefixer
pip install -e .
pip install pytest
pytest tests
```

---

## 📌 PyPI

The package is available at [PyPI - df-datefixer](https://pypi.org/project/df-datefixer/).

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 💬 Feedback & Contributions

Contributions, feedback, and issues are welcome. Open an issue or submit a PR on GitHub!

Enjoy standardizing your dates effortlessly 🎉.
