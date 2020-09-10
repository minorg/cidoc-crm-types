# Python type definitions for the [CIDOC CRM](http://www.cidoc-crm.org/)

This repository contains Python `@dataclass` types generated from the [Erlangen CRM / OWL](http://erlangen-crm.org/) implementation of the CIDOC CRM.

## Structure of the repository

* `circleci/`: [CircleCI](https://circleci.com/) Continuous Integration configuration
* `generator/`: scripts for generating type definitions
* `py/`: Python type definitions

## Generator

### One-time setup

    cd generator
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Running

    cd generator
    source venv/bin/activate
    python3 -m cidoc_crm_types_generator

The generator downloads the current version of the Erlangen CRM `.owl` and then translates it. The command line program accepts various options; run it with `-h` to list them.

## Generated Python

The generated Python code in `py/` consists of a top-level module, `cidoc_crm_types`, with submodules for `entities` (the E1 entity class hierarchy) and `properties` (the property class hierarchy).

The generated code has no dependencies outside the Python standard library, but requires Python 3.7+ for `@dataclass`.
