from .e13_attribute_assignment import E13AttributeAssignment
from dataclasses import dataclass


@dataclass
class E16Measurement(E13AttributeAssignment):
    """
Scope note:
This class comprises actions measuring quantitative physical properties and other values that can be determined by a systematic, objective procedure of direct observation of particular states of physical reality. Properties of instances of E90 Symbolic Object may be measured by observing some of their representative carriers which may or may not be named explicitly. In the case that the carrier can be named, the property P16 used specific object (was used for): should be used to indicate the instance(s) of E18 Physical Thing that was used as the empirical basis for the measurement activity.

Examples include measuring the nominal monetary value of a collection of coins or the running time of a movie on a specific video cassette. The E16 Measurement may use simple counting or tools, such as yardsticks or radiation detection devices. The interest is in the method and care applied, so that the reliability of the result may be judged at a later stage, or research continued on the associated documents. The date of the event is important for dimensions, which may change value over time, such as the length of an object subject to shrinkage. Methods and devices employed should be associated with instances of E16 Measurement by properties such as P33 used specific technique: E29 Design or Procedure, P125 used object of type: E55 Type, P16 used specific object (was used for): E70 Thing, whereas basic techniques such as "carbon 14 dating" should be encoded using P2 has type (is type of): E55 Type. Details of methods and devices reused or reusable in other instances of E16 Measurement should be documented for these entities rather than the measurements themselves, whereas details of particular execution may be documented by free text or by instantiating adequate sub-activities, if the detail may be of interest for an overarching query.

Regardless whether a measurement is made by an instrument or by human senses, it represents the initial transition from physical reality to information without any other documented information object in between within the reasoning chain that would represent the result of the interaction of the observer or device with reality. Therefore, inferring properties of depicted items using image material, such as satellite images, is not regarded as an instance of E16 Measurement, but as a subsequent instance of E13 Attribute Assignment. Rather, only the production of the images, understood as arrays of radiation intensities, is regarded as an instance of E16 Measurement. The same reasoning holds for other sensor data.


Examples:
- measurement of height of silver cup 232 on the 31st  August 1997
- the carbon 14 dating of the ?Schoeninger Speer II? in 1996 [an about 400.000 years old
- Palaeolithic complete wooden spear found in Schoeningen, Niedersachsen, Germany in 1995] (Kouwenhoven, 1997)
- The pixel size of the jpeg version of Titian?s painting Bacchus and Ariadne from 1520?3, as freely downloadable from the National Gallery in London?s web page <https://www.nationalgallery.org.uk/paintings/titian-bacchus-and-ariadne> is 581600 pixels.
- The scope note of E21 Person in the Definition of the CIDOC Conceptual Reference Model Version 5.0.4 as downloaded from <http://www.cidoccrm.org/sites/default/files/cidoc_crm_version_5.0.4.pdf> consists of 77 words.


In First Order Logic:
E16(x) ? E13(x)
    """

    _typename: str = 'E16Measurement'
