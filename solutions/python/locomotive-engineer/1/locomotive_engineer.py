"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return list(args)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    wagon_one, wagon_two, *rest = each_wagons_id
    misplaced_wagons = [wagon_one, wagon_two]
    *shifted_wagons, = *rest, *misplaced_wagons
    locomotive, *wagons = shifted_wagons
    locomotive_list = [locomotive]
    *corrected_wagons, = *locomotive_list, *missing_wagons, *wagons
    return corrected_wagons

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """
    stops_list = list(kwargs.values())
    stops_entry = {"stops":stops_list}
    updated_route_dict = {**route, **stops_entry}
    return updated_route_dict
    
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    extended_route_info = {**route, **more_route_information}
    return extended_route_info


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    updated_wagon_rows = []
    for row in zip(*wagons_rows):
        list_row = list(row)
        updated_wagon_rows.append(list_row)
    return updated_wagon_rows
    
