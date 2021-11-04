from dataclasses import dataclass

@dataclass
class PrefStock:
    """ Preferred Stock Object - Stores attributes of each preferred stock class."""

    name: str
    capital: float  # Original Capital Contribution
    liqpref: float  # Liquidation Preference as multiple of capital
    liqpref_conv: bool = True  # Optional: if liqpref > 1, does multiple convert
    conv_to: str = None  # Optional: Equity class which preferred converts into
    conv_price: float = None  # Optional: Conversion Price
    prefdiv_rate: float = None  # Optional: Preferred dividend rate as percentage (8 for 8%)
    prefdiv_compound: int = 1  # Optional:
    prefdiv_accrues: bool = True
    prefdiv_convert: bool = False
    participation_cp: float = None
    participation_fr: float = None
    participation_cap: float = None




    """

    - Name
    - capital = original capital contribution
    - liqpref = Liquidation Preference Multiple (calc Liquidation Preference)
    Conversion dictionary
    - Converts into
    - Conversion Price (calc converstion rate)
    Preferred Dividend
    - Preferred Dividend
    - Accrues?
    - Preferred Dividend Compounding
    - Dividend convertible
    Participation
    - Participation
    - Participation Conversion Price
    - Participation Fixed Rate (only if not conversion price))
    - Participation Cap

    """



    # def __init__(self, name, capital, liqpref, **kwargs):
    #
    #     __accepted_kwargs = {'conv_to', 'conv_price',
    #                          'prefdiv_rate', 'prefdiv_accrues', 'prefdiv_compound', 'prefdiv_convert',
    #                          'particiption_cp', 'participation_fr', 'participation_cap'}
    #
    #     self.name = name
    #     self.capital = capital
    #     self.liqpref = liqpref
    #
    #     for k in kwargs.keys():
    #         if k in __accepted_kwargs:
    #             self.__setattr__(k, kwargs[k])
    #         else:
    #             print(k, ' is not a valid attribute.')

        # terms = ['conv', 'prefdiv', 'participation']
        #
        # for term in kwargs()
        # self.conv = kwargs.get('conv') or {}
        # self.prefdiv = kwargs.get('prefdiv') or {}
        # self.participation = kwargs.get('participation') or {}
        #

    # def check_kwargs():
    #     for k in kwargs.keys():
    #         if k in __accepted_kwargs:
    #             self.__setattr__(k, kwargs[k])
    #         else:
    #             print(k, ' is not a valid attribute.')
    #
    #     __accepted_kwargs = {'conv':['conv_to', 'conv_price'],
    #                          'prefdiv': ['prefdiv_rate', 'prefdiv_accrues', 'prefdiv_compound', 'prefdiv_convert'],
    #                          'particiption': ['particiption_cp', 'participation_fr', 'participation_cap']}

@dataclass
class CommonStock:
    """ Common Stock Object.

    Stores
    - Name
    - Full Name

    """
    name: 'Common Stock'

class ESO:
    """ Employee Stock Option Object.
    """