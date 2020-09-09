from dataclasses import dataclass


@dataclass
class P72HasLanguage:
    """
Scope note:
This property describes the E56 Language of an E33 Linguistic Object.

Linguistic Objects are composed in one or more human Languages. This property allows these languages to be documented.

Examples:
- the American Declaration of Independence (E33) has language 18th Century English (E56)

In First Order Logic:
P72(x,y) &#8835; E33(x)
P72(x,y) &#8835; E56(y)
    """

    URI = "http://erlangen-crm.org/current/P72_has_language"
