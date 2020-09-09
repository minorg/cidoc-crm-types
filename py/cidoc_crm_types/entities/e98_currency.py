from .e55_type import E55Type
from dataclasses import dataclass


@dataclass
class E98Currency(E55Type):
    """
Scope note:
This class comprises the units in which a monetary system, supported by an administrative authority or other community, quantifies and arithmetically compares all monetary amounts declared in the unit. The unit of a monetary system must describe a nominal value which is kept constant by its administrative authority and an associated banking system if it exists, and not by market value. For instance, one may pay with grams of gold, but the respective monetary amount would have been agreed as the gold price in US dollars on the day of the payment. Under this definition, British Pounds, U.S. Dollars, and European Euros are examples of currency, but &#8220;grams of gold&#8221; is not. One monetary system has one and only one currency. Instances of this class must not be confused with coin denominations, such as &#8220;Dime&#8221; or &#8220;Sestertius&#8221;. Non-monetary exchange of value in terms of quantities of a particular type of goods, such as cows, do not constitute a currency.


Examples:
- &#8220;As&#8221; (Roman mid republic)
- &#8220;Euro&#8221;, (Temperton, 1997)
- &#8220;US Dollar&#8221; (Rose, 1978)


In First Order Logic:
E98(x) &#8835; E55(x)
E98(x) &#8835; E58(x)
    """

    TYPE_URI = "http://erlangen-crm.org/current/E98_Currency"
