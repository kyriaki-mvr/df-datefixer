import pandas as pd
from dateutil import parser

def fix_dates(df, column=None, columns=None, target_format="%Y-%m-%d", missing_value="0",
              verbose=True, convert_to_datetime=False, inplace=False):
    """
    Fixes dates in DataFrame column(s) to a specified format.

    Keyword arguments:
    df -- pandas DataFrame
    column -- column name containing dates (single column)
    columns -- list of column names (multiple columns)
    target_format -- desired date format (default "%Y-%m-%d")
    missing_value -- replacement for missing/unparsable dates (default "0")
    verbose -- print problematic values (default True)
    convert_to_datetime -- converts fixed dates to datetime type if True (default False)
    inplace -- modify DataFrame inplace if True, else returns new DataFrame (default False)
    :return: DataFrame with fixed date column(s)
    """
    if not inplace:
        df = df.copy()

    cols = columns if columns else [column]

    missing_value_str = str(missing_value)

    for col in cols:
        fixed_dates, problems = [], []
        for idx, val in df[col].items():
            if pd.isnull(val):
                problems.append((idx, "None (missing)"))
                fixed_dates.append(None)  # temporarily None for accurate datetime handling
                continue
            try:
                parsed_date = parser.parse(str(val))
                fixed_dates.append(parsed_date.strftime(target_format))
            except Exception:
                problems.append((idx, val))
                fixed_dates.append(None)

        if verbose and problems:
            print(f"! {len(problems)} problematic date values found in column \"{col}\":")
            for idx, issue in problems:
                print(f"- Row {idx}: {issue}")

        if convert_to_datetime:
            df[col] = pd.to_datetime(fixed_dates, errors="coerce")
            df[col] = df[col].fillna(missing_value_str)
        else:
            df[col] = [val if val is not None else missing_value_str for val in fixed_dates]

    return df