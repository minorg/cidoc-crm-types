from .p106_is_composed_of import P106IsComposedOf
from dataclasses import dataclass


@dataclass
class P165Incorporates(P106IsComposedOf):
    """
Scope note: 
This property associates an instance of E73 Information Object with an instance of E90 Symbolic Object (or any of its subclasses) that was included in it.

This property makes it possible to recognise the autonomous status of the incorporated signs, which were created in a distinct context, and can be incorporated in many distinct self-contained expressions, and to highlight the difference between structural and accidental whole-part relationships between conceptual entities.

It accounts for many cultural facts that are quite frequent and significant: the inclusion of a poem in an anthology, the re-use of an operatic aria in a new opera, the use of a reproduction of a painting for a book cover or a CD booklet, the integration of textual quotations, the presence of lyrics in a song that sets those lyrics to music, the presence of the text of a play in a movie based on that play, etc.

In particular, this property allows for modelling relationships of different levels of symbolic specificity, such as the natural language words making up a particular text, the characters making up the words and punctuation, the choice of fonts and page layout for the characters.

When restricted to information objects, that is, seen as a property with E73 Information Object as domain and range the property is transitive.

A digital photograph of a manuscript page incorporates the text of a manuscript page, if the respective text is defined as a sequence of symbols of a particular type, such as Latin characters, and the resolution and quality of the digital image is sufficient to resolve these symbols so they are readable on the digital image.


Examples:	
- The content of Charles-Mo&#239;se Briquet&#8217;s &#8216;Les Filigranes: dictionnaire historique des marques du papier&#8217; (E32) P165 incorporates the visual aspect of the watermark used around 1358-61 by some Spanish papermaker(s) and identified as &#8216;Briquet 4019&#8217; (E37)
- The visual content of Jacopo Amigoni&#8217;s painting known as &#8216;The Singer Farinelli and friends&#8217; (E36) P165 incorporates the musical notation of Farinelli&#8217;s musical work entitled &#8216;La Partenza&#8217; (E73)
- The visual content of Nicolas Poussin&#8217;s painting entitled &#8216;Les Bergers d&#8217;Arcadie&#8217; (E36) P165 incorporates the Latin phrase &#8216;Et in Arcadia ego&#8217; (E33)


In First Order Logic:
P165(x,y) &#8835; E73(x)
P165(x,y) &#8835; E90(y)
P165(x,y) &#8835; P106(x,y)
    """

    URI = "http://erlangen-crm.org/current/P165_incorporates"
