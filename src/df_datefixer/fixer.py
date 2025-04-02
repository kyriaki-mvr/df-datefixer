import pandas as pd
from dateutil import parser

def fix_dates(df, column, target_format="%Y-%m-%d", missing_value="0", verbose=True):
    """
    Fixes dates in a DataFrame column to a specified format.

    Keyword arguments:
    df -- input pandas DataFrame
    column -- name of the column with dates to fix
    target_format -- desired date format (default "%Y-%m-%d")
    missing_value -- value to use for invalid or missing dates (default "0")
    verbose -- print problematic values (default True)

    :return: DataFrame with fixed date column
    """
    fixed_dates = []
    problems = []

    for idx, val in df[column].items():
        if pd.isnull(val):
            problems.append((idx, "None (missing)"))
            fixed_dates.append(missing_value)
            continue
        try:
            parsed_date = parser.parse(str(val))
            fixed_dates.append(parsed_date.strftime(target_format))
        except Exception:
            problems.append((idx, val))
            fixed_dates.append(missing_value)

    if verbose and problems:
        print(f"⚠️ {len(problems)} problematic date values found in column '{column}':")
        for idx, issue in problems:
            print(f"- Row {idx}: {issue}")

    df[column] = fixed_dates
    return df
