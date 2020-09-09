from dataclasses import dataclass


@dataclass
class P152HasParent:
    """
Scope note:
This property associates an instance of E21 Person with another instance of E21 Person who plays the role of the first instance&#8217;s parent, regardless of whether the relationship is biological parenthood, assumed or pretended biological parenthood or an equivalent legal status of rights and obligations obtained by a social or legal act. This property is, among others, a shortcut of the fully developed paths from &#8216;E21Person&#8217; through &#8216;P98i was born&#8217;, &#8216;E67 Birth&#8217;, &#8216;P96 by mother&#8217; to &#8216;E21 Person&#8217;, and from &#8216;E21Person&#8217; through &#8216;P98i was born&#8217;, &#8216;E67 Birth&#8217;, &#8216;P97 from father&#8217; to &#8216;E21 Person&#8217;.


Examples:
- Gaius Octavius (E21) has parent Julius Caesar (E21)
- Steve Jobs (E21) has parent Joanne Simpson (biological mother) (E21)
- Steve Jobs (E21) has parent Clara Jobs (adoption mother) (E21)


In First Order Logic:
P152(x,y) &#8835; E21(x)
P152(x,y) &#8835; E21(y)
    """

    URI = "http://erlangen-crm.org/current/P152_has_parent"
