import data_fetcher


def get_user_animal():
    """asks the user for an animal and returns the answer"""
    animal = input("Enter a name of an animal: ")
    return animal


def read_html_template(html_path):
    """reads a html template file"""
    with open(html_path, "r", encoding="utf-8") as html_file:
        return html_file.read()


def write_new_html(html_string, filename):
    """writes a new html file"""
    with open(filename, "w", encoding="utf-8") as new_html_file:
        new_html_file.write(html_string)
    print(f"Website was successfully generated to the file {filename}.")


def get_data_from_file(animal):
    """gets the value of the fields name, diet, first location and type from
    one animal of the animal data"""
    animal_name = animal.get("name")
    animal_taxonomy = animal.get("taxonomy")
    animal_scientific_name = animal_taxonomy.get("scientific_name")
    animal_characteristics = animal.get("characteristics")
    animal_diet = animal_characteristics.get("diet")
    animal_slogan = animal_characteristics.get("slogan")
    animal_location = animal.get("locations")[0]
    animal_type = animal_characteristics.get("type")
    animal_hair = animal_characteristics.get("skin_type")
    dict_data = {
        "Scientific name": animal_scientific_name,
        "Diet": animal_diet,
        "Location": animal_location,
        "Type": animal_type,
        "Animal hair": animal_hair,
        "Slogan": animal_slogan,
    }
    return animal_name, dict_data


def serialize_animal(animal_obj):
    """creates a html card for an item"""
    output = ""
    output += '<li class="cards__item">\n'
    a_name, data = get_data_from_file(animal_obj)
    output += f'<div class ="card__title"> {a_name} </div>\n'
    output += '<div class="card__text">\n'
    output += '<ul style="margin-top: 20px; font-size: 16px">'
    for label, value in data.items():
        if value:
            output += (
                f'<li style="list-style-type: square; line-height: '
                f'2.5"><strong>{label}:</strong> {value}</li>\n'
            )
    output += "</ul>\n"
    output += "</div>\n"
    output += "</li>\n"
    output = output.replace("’", "'")
    return output


def create_html_animal(name, data):
    """adds the animals information in a given html template"""
    if not data:
        output = f"<h2>The animal {name} doesn't exist.</h2>"
    else:
        output = ""
        for animal in data:
            output += serialize_animal(animal)
    html_data = read_html_template("animals_template.html")
    return html_data.replace("__REPLACE_ANIMALS_INFO__", output)


def get_skin_type(animal_item):
    """returns the skin type attribute from an animal item in a json data"""
    animal_characteristics = animal_item.get("characteristics")
    animal_skin_type = animal_characteristics.get("skin_type")
    return animal_skin_type


def get_available_skin_types(animals_data):
    """creates a list with the available skin type in a json data"""
    available_skin_types = []
    for animal in animals_data:
        a_skin_type = get_skin_type(animal)
        if a_skin_type not in available_skin_types:
            available_skin_types.append(a_skin_type)
    return available_skin_types


def filter_data_by_skin_type(data, skin_type):
    """creates a dictionary only with the animals with the desired skin_type"""
    new_data = [item for item in data if get_skin_type(item) == skin_type]
    return new_data


def get_user_choice_skin_type(available_skin_types):
    """asks tje user to enter a skin type from a list and the user choice is
    returned"""
    output_skin_types = ""
    for skin_item in enumerate(available_skin_types):
        index, skin_type = skin_item
        output_skin_types += skin_type
        if index != len(available_skin_types) - 1:
            output_skin_types += ", "
    while True:
        user_choice = input(
            "Please choose a skin type: " + output_skin_types + " ")
        user_choice_lower = user_choice.lower()
        if user_choice_lower.title() in available_skin_types:
            return user_choice_lower.title()
        print("Please enter an available choice from the list.")


def filter_structure_skin_type(name, animals_data):
    """asks the user if he wants to create a website for the animals that
    have a particular skin type, if yes then the skin type choice is asked.
    The function creates a html file with the animals with the skin type
    choice filtered from the json data"""
    while True:
        user_answer = input(
            "Do you want to create a website only for the animals "
            "with a particular skin type? (y/n) "
        )
        if user_answer.lower() == "y":
            available_skin_types = get_available_skin_types(animals_data)
            user_choice = get_user_choice_skin_type(available_skin_types)
            data_filtered_skin_type = filter_data_by_skin_type(
                animals_data, user_choice
            )
            filtered_html_filename = "animal_" + user_choice.lower() + ".html"
            html_filtered_data = create_html_animal(name, data_filtered_skin_type)
            html_filtered_data = html_filtered_data.replace(
                "My Animal Repository", f"{name} with " + user_choice
            )
            write_new_html(html_filtered_data, filtered_html_filename)
        elif user_answer.lower() == "n":
            print("Maybe another time.")
            break
        else:
            print("The input is not correct, you have to write y or n.")


def main():
    user_animal = get_user_animal()
    animals_data = data_fetcher.fetch_data(user_animal)
    if animals_data:
        html_new_data = create_html_animal(user_animal, animals_data)
        write_new_html(html_new_data, "animals.html")
        filter_structure_skin_type(user_animal, animals_data)


if __name__ == "__main__":
    main()
