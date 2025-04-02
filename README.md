# df-datefixer 📅

[![PyPI](https://img.shields.io/pypi/v/df-datefixer.svg)](https://pypi.org/project/df-datefixer/)
[![License](https://img.shields.io/github/license/kyriaki-mvr/df-datefixer)](LICENSE)

A lightweight Python library to standardize date columns in Pandas DataFrames. It automatically handles multiple date formats, missing values, and problematic entries.

## Installation

Install via pip:

```shell
pip install df-datefixer
```

## Usage

```python
import pandas as pd
from df_datefixer.fixer import fix_dates

df = pd.DataFrame({
    'event_date': ['2022-01-01', '1/2/2022', 'bad-date', None]
})

fixed_df = fix_dates(df, column="event_date", target_format="%Y-%m-%d", missing_value="0")

print(fixed_df)
```

The above will print:

```
⚠️ 2 problematic date values found in column "event_date":
- Row 2: bad-date
- Row 3: None (missing)

  event_date
0  2022-01-01
1  2022-01-02
2           0
3           0
```

## Parameters

- `df`: A pandas DataFrame.
- `column`: Column name containing dates.
- `target_format`: Desired standardized date format (default is "%Y-%m-%d").
- `missing_value`: Replacement for missing/unparsable dates (default is "0").
- `verbose`: Print details about problematic dates (default is `True`).

## Development

Clone and install in editable mode for local development:

```shell
git clone https://github.com/kyriaki-mvr/df-datefixer.git
cd df-datefixer
pip install -e .
pip install pytest
pytest tests
```

## PyPI

See the package on [PyPI - df-datefixer](https://pypi.org/project/df-datefixer/).

## License

`df-datefixer` is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions and issues are welcome! Please open an issue or submit a pull request on GitHub.