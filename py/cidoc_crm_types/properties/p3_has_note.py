from dataclasses import dataclass


@dataclass
class P3HasNote:
    """
Scope note:
This property is a container for all informal descriptions about an object that have not been expressed in terms of CRM constructs.

In particular it captures the characterisation of the item itself, its internal structures, appearance etc.
Like property P2 has type (is type of), this property is a consequence of the restricted focus of the CRM. The aim is not to capture, in a structured form, everything that can be said about an item; indeed, the CRM formalism is not regarded as sufficient to express everything that can be said. Good practice requires use of distinct note fields for different aspects of a characterisation. The P3.1 has type property of P3 has note allows differentiation of specific notes, e.g. "construction", "decoration" etc.
An item may have many notes, but a note is attached to a specific item.

Examples:
- coffee mug - OXCMS:1983.1.1 (E19) has note "chipped at edge of handle" (E62) has type
Condition (E55)

In First Order Logic:
P3(x,y) &#8835; E1(x)
P3(x,y) &#8835; E62(y)
P3(x,y,z) &#8835; [P3(x,y) &#8743; E55(z)]

Properties: P3.1 has type: E55 Type
    """

    URI = "http://erlangen-crm.org/current/P3_has_note"
