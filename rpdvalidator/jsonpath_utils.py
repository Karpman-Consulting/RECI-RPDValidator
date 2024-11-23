from itertools import chain
from jsonpath_ng.ext import parse


def find_all(jpath, obj):
    """
    Find all values matching a JSONPath expression within a JSON object using jsonpath.

    Args:
        jpath (str): JSONPath string.
        obj (dict): JSON object to search.

    Returns:
        list: List of values matching the JSONPath expression.
    """
    jsonpath_expr = parse(jpath)
    return [match.value for match in jsonpath_expr.find(obj)]


def find_all_by_jsonpaths(jpaths: list, obj: dict) -> list:
    return list(chain.from_iterable([find_all(jpath, obj) for jpath in jpaths]))


def json_paths_to_lists(val, path="$"):
    """Determines all the generic json paths to lists inside an object

    If a json path has a list index, that index is replaced with [*] to make it
    generic.

    Parameters
    ----------
    val : any
        Only dict and list objects are processed, all others are ignored
    path : str
        A json path representing a generic path to val in a larger structure

    Returns
    -------
    set
        A set of unique generic json paths to lists inside val
    """
    paths = set()
    if isinstance(val, dict):
        paths = json_paths_to_lists_from_dict(val, path)
    elif isinstance(val, list):
        paths = json_paths_to_lists_from_list(val, path)

    return paths


def json_paths_to_lists_from_dict(rpd_dict, path):
    """Determines all the generic json paths to lists inside a dictionary

    If a json path has a list index, that index is replaced with [*] to make it
    generic.

    Parameters
    ----------
    rpd_dict : dict

    path : str
        A json path representing a generic path to rpd_dict in a larger structure

    Returns
    -------
    set
        A set of unique generic json paths to lists inside rpd_dict
    """
    paths = set()
    for key, val in rpd_dict.items():
        new_path = f"{path}.{key}"
        new_paths = json_paths_to_lists(val, new_path)
        paths = paths.union(new_paths)

    return paths


def json_paths_to_lists_from_list(rpd_list, path):
    """Determines all the generic json paths to lists inside a list

    If a json path has a list index, that index is replaced with [*] to make it
    generic.

    Parameters
    ----------
    rpd_list : list

    path : str
        A json path representing a generic path to rpd_list in a larger structure

    Returns
    -------
    set
        A set of unique generic json paths to lists inside rpd_list
    """
    paths = {path}
    for val in rpd_list:
        new_path = f"{path}[*]"
        new_paths = json_paths_to_lists(val, new_path)
        paths = paths.union(new_paths)

    return paths


def convert_absolute_path_list_to_jsonpath(input_list):
    jsonpath = "$"  # Start with the root '$'
    for i, item in enumerate(input_list):
        if isinstance(item, str):
            jsonpath += f".{item}"  # Append strings as keys
        elif isinstance(item, int):
            jsonpath += f"[{item}]"  # Append integers as array indices

    return jsonpath


def format_jsonpath_with_id(input_list):
    if not input_list:
        return
    # Replace the last item in the list with 'id'
    input_list = input_list[:-1] + ['id']
    return convert_absolute_path_list_to_jsonpath(input_list)
