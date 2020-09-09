from .p3_has_note import P3HasNote
from dataclasses import dataclass


@dataclass
class P190HasSymbolicContent(P3HasNote):
    """
Scope note: 
This property associates an instance of E90 Symbolic Object with a complete, identifying representation of its content in the form of an instance of E62 String.
This property only applies to instances of E90 Symbolic Object that can be represented completely in this form. The representation may be more specific than the symbolic level defining the identity condition of the represented. This depends on the type of the symbolic object represented. For instance, if a name has type "Modern Greek character sequence", it may be represented in a loss-free Latin transcription, meaning however the sequence of Greek letters.
As another example, if the represented object has type "English words sequence", American English or British English spelling variants may be chosen to represent the English word "colour" without defining a different symbolic object. If a name has type "European traditional name", no particular string may define its content.

Examples:
- The materials description (E33) of the painting has symbolic content &#8220;Oil, French Watercolors on Paper, Graphite and Ink on Canvas, with an Oak frame.&#8221;
- The title (E35) of Einstein&#8217;s 1915 text has symbolic content &#8220;Relativity, the Special and the General Theory &#8220;
- The story of Little Red Riding Hood (E33) has symbolic content &#8220;Once upon a time there lived in a certain village &#8230;&#8221;
- The inscription (E34) on Rijksmuseum object SK-A-1601 has symbolic content &#8220;B&#8221;


In First Order Logic:
P190(x,y) &#8835; E90(x)
P190(x,y) &#8835; E62(y)
    """

    URI = "http://erlangen-crm.org/current/P190_has_symbolic_content"
