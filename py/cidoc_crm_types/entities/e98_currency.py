from .e58_measurement_unit import E58MeasurementUnit
from dataclasses import dataclass


@dataclass
class E98Currency(E58MeasurementUnit):
    """
Scope note:
This class comprises the units in which a monetary system, supported by an administrative authority or other community, quantifies and arithmetically compares all monetary amounts declared in the unit. The unit of a monetary system must describe a nominal value which is kept constant by its administrative authority and an associated banking system if it exists, and not by market value. For instance, one may pay with grams of gold, but the respective monetary amount would have been agreed as the gold price in US dollars on the day of the payment. Under this definition, British Pounds, U.S. Dollars, and European Euros are examples of currency, but ?grams of gold? is not. One monetary system has one and only one currency. Instances of this class must not be confused with coin denominations, such as ?Dime? or ?Sestertius?. Non-monetary exchange of value in terms of quantities of a particular type of goods, such as cows, do not constitute a currency.


Examples:
- ?As? (Roman mid republic)
- ?Euro?, (Temperton, 1997)
- ?US Dollar? (Rose, 1978)


In First Order Logic:
E98(x) ? E55(x)
E98(x) ? E58(x)
    """

    __typename: str = 'E98Currency'
