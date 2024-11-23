import os
import json
import argparse
from rpdvalidator.validate import schema_validate, validate_references


def validate_rpd(rpd):
    """Validate an RPD against the schema and other high-level checks"""
    result = schema_validate(rpd)

    if result["passed"]:
        result = validate_references(rpd)

    return result


def validate():
    parser = argparse.ArgumentParser(description="Validate an RPD file against a schema.")
    parser.add_argument("rpd_file", type=str, help="Path to the RPD file to validate.")
    parser.add_argument("--version", type=str, default="0.1.0", help="Schema version to use (default: 0.1.0).")

    args = parser.parse_args()

    # Check that the RPD file exists
    if not os.path.exists(args.rpd_file):
        print(f"Error: RPD file '{args.rpd_file}' does not exist.")
        exit(1)

    with open(args.rpd_file) as rpd_file:
        try:
            rpd = json.load(rpd_file)
        except json.JSONDecodeError as e:
            print(f"Error: Failed to parse RMD file '{args.rmd_file}': {e}")
            exit(1)

    result = schema_validate(rpd, schema_version=args.version)

    if result["passed"]:
        print("Validation: PASS.")
        exit(0)

    else:
        print("Validation: FAIL. Errors:")
        for error in result['errors']:
            print(f"- {error}")
        exit(1)


if __name__ == "__main__":
    exit(validate())
