# RECI-RPDValidator

**RECI-RPDValidator** is a Python utility designed to validate Ruleset Project Description (RPD) files against requirements established by the ASHRAE 229 schema. It supports multiple schema versions, ensuring compatibility and compliance across various releases.  

By default, the utility validates RPD files against version `0.1.0` of the ASHRAE 229 schema. If the validation fails, a detailed report of all errors encountered will be provided.

This project is an adaptation of a feature included in the Ruleset Checking Tool, created by PNNL.
We have made modifications including explicit support of multiple versions of the schema, and enhance the validation error messages.
All credit for the original work goes to PNNL. For more details, visit https://github.com/pnnl/ruleset-checking-tool.

This project uses jsonpath-ng, which is licensed under the Apache License 2.0.

---

## Features

- Validate RPD files for compliance with the ASHRAE 229 schema.
- Support for multiple schema versions.
- Clear and comprehensive error reporting for failed validations.

---

## Installation

**Requirements:**

- Python 3
- jsonpath-ng
- jsonschema
- referencing

To install, you can use the command:

```bash
pip install rpdvalidator
```

---

## Usage

### Command-Line Utility

RECI-RPDValidator provides a straightforward command-line interface for validating RPD files. Use the following command to validate an RPD file:

```bash
validateRPD rpd-filename.json
```

**Specifying a Schema Version**  
To validate an RPD file against a specific schema version, use the `--version` flag:

```bash
validateRPD rpd-filename.json --version 0.2.0
```
If no version is specified, the utility defaults to schema version `0.1.0`.


### Python

You can also use the utility as a Python module. Here's an example of how to validate an RPD file:

```python
from rpdvalidator import validate_rpd

rpd_file = "path/to/rpd-filename.json"
validate_rpd(rpd_file)
```

**Specifying a Schema Version**  
To validate an RPD file against a specific schema version, provide the version as an argument:

```python
from rpdvalidator import validate_rpd

rpd_file = "path/to/rpd-filename.json"
schema_version = "0.2.0"
validate_rpd(rpd_file, schema_version)
```


---

## Output

- **passed**: Boolean indicating if the RPD file is valid.
- **errors**: A list of errors found during validation.

---

## Disclaimer Notice      
- Acknowledgment: This material is based upon work supported by the U.S. Department of Energy’s Office of Energy Efficiency and Renewable Energy (EERE) under the Building Technologies Office - DE-FOA-0002813 - Bipartisan Infrastructure Law Resilient and Efficient Codes Implementation.  
- Award Number: DE-EE0010949  
- Abridged Disclaimer:  The views expressed herein do not necessarily represent the view of the U.S. Department of Energy or the United States Government.  