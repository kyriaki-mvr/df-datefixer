# df-datefixer

[![PyPI](https://img.shields.io/pypi/v/df-datefixer.svg)](https://pypi.org/project/df-datefixer/)
[![PyPI Downloads](https://static.pepy.tech/badge/df-datefixer)](https://pepy.tech/projects/df-datefixer)

A lightweight Python library to standardize date columns in Pandas DataFrames. It automatically handles multiple date formats, missing values, problematic entries, multi-column fixing, optional datetime conversion, and more.

See the package on [PyPI](https://pypi.org/project/df-datefixer/).\
See the package on [GitHub](https://github.com/kyriaki-mvr/df-datefixer)

## Installation

Install via pip:

```shell
pip install df-datefixer
```

## Usage

Basic usage:

```python
import pandas as pd
from df_datefixer.fixer import fix_dates

df = pd.DataFrame({
    'event_date': ['2022-01-01', '1/2/2022', 'bad-date', None]
})

fixed_df = fix_dates(df, column="event_date", target_format="%Y-%m-%d", missing_value="0")

print(fixed_df)
```

### Multiple columns, datetime conversion, and custom placeholders:

```python
df = pd.DataFrame({
    'start_date': ['2022-01-01', '1/2/2022', 'bad-date', None],
    'end_date': ['2022-02-01', 'invalid', '03-03-2022', None]
})

fixed_df = fix_dates(df, columns=['start_date', 'end_date'], convert_to_datetime=True, missing_value="NaT")

print(fixed_df)
```

### Important note about datetime conversion:

If you set `convert_to_datetime=True` with a custom `missing_value`, your column might be converted to object type instead of datetime, because custom placeholders might not be datetime-compatible. For pure datetime operations, leaving `missing_value` as `"NaT"` (default datetime placeholder) is recommended.

## Parameters

- `df`: A pandas DataFrame
- `column`: Column name containing dates (single column)
- `columns`: List of column names to fix simultaneously
- `target_format`: Desired standardized date format (default is "%Y-%m-%d")
- `missing_value`: Replacement for missing/unparsable dates (default is "0")
- `verbose`: Print details about problematic dates (default is `True`)
- `convert_to_datetime`: Converts fixed dates to pandas datetime type if `True` (default is `False`)
- `inplace`: Modifies DataFrame in place if `True`, else returns a new DataFrame (default is `False`)

## Development

### Set up virtual environment

```shell
python -m venv venv
source venv/bin/activate  # on macOS/Linux
.\venv\Scripts\activate  # on Windows
```

### Clone repository and install dependencies

```shell
git clone https://github.com/kyriaki-mvr/df-datefixer.git
cd df-datefixer
pip install -e .
pip install pytest
```

### Run tests

```shell
pytest tests
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## Feedback

If you have any feedback, please file an issue on the GitHub repository page. I am always looking to improve and appreciate all feedback, bug reports, and suggestions.

## Authors

Kyriaki Mavropoulou (kyriaki@quanterra.gr) - Initial work

## License

`df-datefixer` is licensed under the MIT License - see the LICENSE file for details.
