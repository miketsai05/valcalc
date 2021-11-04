import datetime
from dataclasses import dataclass
from typing import List

import pandas as pd

import equityclasses


@dataclass
class CapTableRow:
    equityclass: object
    numshares: int
    liqpref_seniority: int = None
    issuedate: datetime.date = None
    pastdist: float = 0.


@dataclass
class CapTable:
    captable_rows: List[CapTableRow]
    captable_date: datetime.date

    def to_df(self):
        df = pd.DataFrame(self.captable_rows)
        df = pd.DataFrame(df.equityclass.values.tolist()).join(df.drop('equityclass',axis=1))
        return df

    def gen_breakpoints(self):
        """ Creates breakpoints """



if __name__ == 'main':

    common = equityclasses.CommonStock('common')
    prefA = equityclasses.PrefStock('Series A', 100, 1, conv_to='common', conv_price=100, prefdiv_rate=8)
    prefB = equityclasses.PrefStock('Series B', 200, 1, conv_to='common', conv_price=200, prefdiv_rate=8)

    equity = {'common': common, 'prefA': prefA, 'prefB': prefB}

    rows = [CapTableRow(common, 500, 3), CapTableRow(prefA, 100, 2), CapTableRow(prefB, 100, 1)]

    captable_20211104 = CapTable(rows, datetime.date(2021, 11, 4))

    check = captable_20211104.to_df()




"""
Checks:
    - if prefdiv not 0 then need issuedate
    - if each of conv, prefdiv, participation not None then need the other relevant fields

"""

