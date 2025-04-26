import pandas as pd
import pytest
from df_datefixer.fixer import fix_dates

def test_fix_dates_basic():
    df = pd.DataFrame({
        'dates': ['2022-01-01', '01/02/2022', 'bad-date', None]
    })
    fixed_df = fix_dates(df, column="dates", verbose=False)
    assert fixed_df['dates'].tolist() == ['2022-01-01', '2022-01-02', '0', '0']

def test_fix_dates_convert_to_datetime():
    df = pd.DataFrame({'dates': ['2022-01-01', '1/2/2022']})
    result = fix_dates(df, column="dates", convert_to_datetime=True, verbose=False)
    assert pd.api.types.is_datetime64_any_dtype(result['dates'])

def test_fix_dates_multiple_columns():
    df = pd.DataFrame({
        'start_date': ['2022-01-01', 'bad'],
        'end_date': ['2022-01-03', None]
    })
    result = fix_dates(df, columns=['start_date', 'end_date'], verbose=False)
    assert result["start_date"].tolist() == ['2022-01-01', '0']
    assert result["end_date"].tolist() == ['2022-01-03', '0']

def test_fix_dates_custom_format():
    df = pd.DataFrame({
        'dates': ['2022-01-01', '1/2/2022']
    })
    fixed_df = fix_dates(df, column="dates", target_format="%d-%m-%Y", verbose=False)
    assert fixed_df['dates'].tolist() == ['01-01-2022', '02-01-2022']

def test_fix_dates_no_problems():
    df = pd.DataFrame({
        'dates': ['2022-01-01', '2022-01-02']
    })
    fixed_df = fix_dates(df, column="dates", verbose=False)
    assert fixed_df['dates'].tolist() == ['2022-01-01', '2022-01-02']

def test_fix_dates_missing_values_custom_placeholder():
    df = pd.DataFrame({
        'dates': [None, 'not a date']
    })
    fixed_df = fix_dates(df, column="dates", missing_value="missing", verbose=False)
    assert fixed_df['dates'].tolist() == ['missing', 'missing']

def test_fix_dates_verbose_output(capsys):
    df = pd.DataFrame({
        'dates': ['2022-01-01', 'invalid-date']
    })
    fix_dates(df, column="dates", verbose=True)
    captured = capsys.readouterr()
    assert "problematic date values" in captured.out
    assert "invalid-date" in captured.out

def test_fix_dates_empty_dataframe():
    df = pd.DataFrame({'dates': []})
    fixed_df = fix_dates(df, column="dates", verbose=False)
    assert fixed_df.empty

def test_fix_dates_column_not_exist():
    df = pd.DataFrame({'not_dates': ['2022-01-01']})
    with pytest.raises(KeyError):
        fix_dates(df, column="dates", verbose=False)

def test_fix_dates_missing_value_int():
    df = pd.DataFrame({'dates': [None, 'invalid-date']})
    fixed_df = fix_dates(df, column="dates", missing_value=0, verbose=False)
    assert fixed_df['dates'].tolist() == ['0', '0']
    assert all(isinstance(val, str) for val in fixed_df['dates'])

def test_fix_dates_inplace():
    df = pd.DataFrame({'dates': ['2022-01-01', 'bad-date']})
    fix_dates(df, column="dates", inplace=True, verbose=False)
    assert df["dates"].tolist() == ['2022-01-01', '0']
