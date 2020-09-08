from .e8_acquisition import E8Acquisition
from dataclasses import dataclass
from typing import Tuple


@dataclass
class E96Purchase(E8Acquisition):
    """
Scope note:
This class comprises transfers of legal ownership from one or more instances of E39 Actor to one or more different instances of E39 Actor, where the transferring party is completely compensated by the payment of a monetary amount. In more detail, a purchase agreement establishes a fixed monetary obligation at its initialization on the receiving party, to the giving party. An instance of E96 Purchase begins with the contract or equivalent agreement and ends with the fulfilment of all contractual obligations. In the case that the activity is abandoned before both parties have fulfilled these obligations, the activity is not regarded as an instance of E96 Purchase.

This class is a very specific case of the much more complex social business practices of exchange of goods and the creation and satisfaction of related social obligations. Purchase activities which define individual sales prices per object can be modelled by instantiating E96 Purchase for each object individually and as part of an overall instance of E96 Purchase transaction.


In First Order Logic:
E96(x) ? E8(x)
    """

    P179_had_sales_price: Tuple[object, ...] = ()  # Range: E97MonetaryAmount
    __typename: str = 'E96Purchase'
