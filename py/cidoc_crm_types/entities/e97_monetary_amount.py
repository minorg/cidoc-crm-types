from .e54_dimension import E54Dimension
from dataclasses import dataclass


@dataclass
class E97MonetaryAmount(E54Dimension):
    """
Scope note:
This class comprises quantities of monetary possessions or obligations in terms of their nominal value with respect to a particular currency. These quantities may be abstract accounting units, the nominal value of a heap of coins or bank notes at the time of validity of the respective currency, the nominal  Definition of the CIDOC Conceptual Reference Model version 6.2.8 44 value of a bill of exchange or other documents expressing monetary claims or obligations. It specifically excludes amounts expressed in terms of weights of valuable items, like gold and diamonds, and quantities of other non-currency items, like goats or stocks and bonds. 


Example:
- Christies&#8217; hammer price for &#8220;Vase with Fifteen Sunflowers&#8221; (E97) has currency British Pounds (E98)


In First Order Logic:
E97(x) &#8835; E54(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E97_Monetary_Amount"
