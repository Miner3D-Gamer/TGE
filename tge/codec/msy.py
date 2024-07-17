# Miner3D's Simplified YAML
def parse_msy(data: str) -> dict:
    """
    Returns a dictionary based on the inputted string (msy format)
    """
    parsed_data = {}
    current_list_name = None

    lines = data.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("#"):
            current_list_name = line[1:].strip()
            parsed_data[current_list_name] = []
        elif line:
            if current_list_name is not None:
                parsed_data[current_list_name].append(line)
            else:
                raise ValueError("Data format error: Item found before list name.")

    return parsed_data


def format_msy(data: dict) -> str:
    """
    Returns a a str (msy formatted) from the inputted dictionary
    """
    formatted_text = ""

    for list_name, items in data.items():
        formatted_text += f"#{list_name}\n"
        for item in items:
            formatted_text += f"{item}\n"
        formatted_text += "\n"

    return formatted_text