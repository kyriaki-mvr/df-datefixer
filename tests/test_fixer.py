import pandas as pd
from df_datefixer.fixer import fix_dates

def test_fix_dates():
    df = pd.DataFrame({
        'dates': ['2022-01-01', '01/02/2022', 'bad-date', None]
    })

    result_df = fix_dates(df, column="dates", verbose=False)

    expected = ['2022-01-01', '2022-01-02', '0', '0']
    assert result_df['dates'].tolist() == expected
