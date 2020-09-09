from .p16_used_specific_object import P16UsedSpecificObject
from dataclasses import dataclass


@dataclass
class P142UsedConstituent(P16UsedSpecificObject):
    """
Scope note:
This property associates an instance of E15 Identifier Assignment with the instance of E90 Symbolic Object used as constituent of an instance of E42 Identifier in this act of assignment.


Examples:
- On June 1, 2001 assigning the personal name identifier &#8220;Guillaume, de Machaut, ca. 1300-1377&#8221; (E15) used constituent &#8220;ca. 1300-1377&#8221; (E41) 
- Assigning a uniform title to the anonymous textual work known as &#8216;The Adoration of the Shepherds&#8217;(E15) used constituent &#8216;Coventry&#8217; (E41) 
- Assigning a uniform title to Pina Bausch&#8217;s choreographic work entitled &#8216;Rite of spring&#8217; (E15) used constituent &#8216;(Choreographic Work: Bausch)&#8217;(E90) 
- Assigning a uniform title to the motion picture directed in 1933 by Merian C. Cooper and Ernest B. Schoedsack and entitled &#8216;King Kong&#8217; (E15) used constituent &#8216;1933&#8217; (E41) 
- Assigning the corporate name identifier &#8216;Univerza v Ljubljani. Oddelek za bibliotekarstvo&#8217; to The Department for library science of the University of Ljubljana (E15) used constituent &#8216;Univerza v Ljubljani&#8217; (E42)


In First Order Logic:
P142(x,y) &#8835; E15(x)
P142(x,y) &#8835; E90(y)
P142(x,y) &#8835; P16(x,y)
    """

    URI = "http://erlangen-crm.org/current/P142_used_constituent"
