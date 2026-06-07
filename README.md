# **zootopia_with_api**

---

A web generator of animal information built with Python.

## **Description**

___

This project was developed as a practice assessment for a Software Engineering Bootcamp in Masterschool.
It demonstrates:

- the integration of external APIs
- python requests
- static website generation

## **Overview**

"zootopia_with_api" allows users to generate an HTML file with the information of an animal.

The user is asked to enter the name of an animal. The information of all the kinds of animals with this name is fetched through the API Ninjas and organized in an html file.

The user can decide also to generate another HTML file with the information of these animals, but only of the ones with a particular type of skin.

## **Features**

___

- Search for animals by name through command line.
- Retrieve animal information from an external API.
- Automatic generation of informative animal webpages.
- possibility of generating web pages for an animal with a specific type of skin.

## Technologies Used

___

| Technology | Purpose                                  |
|:-----------|:-----------------------------------------|
| Python     | Core application                         | 
| HTML       | Generated movie website                  |

## **How It Works** ##

___

1. Enter an animal.
2. The application retrieves the animal information.
3. A webpage with the animal information is generated.
4. The user is asked if a webpage of the animal with a specific type of skin is needed.
5. In that case the user is asked to enter the kind of skin from a list of available types of skin.
6. A webpage with the animal information with the selected kind of skin is generated.

## **Installation**

___

1. Get a free API Key at https://api-ninjas.com/
2. Clone the repository:

```
git clone https://github.com/esterplaza/zootopia_with_api.git
```

3. Install requirements:

```
pip install -r requirements.txt
```

4. Configuration

This project requires an API key to access the animal data service.

Create a .env file in the project root directory:
```
API_KEY="your_api_key_here"
```
Replace your_api_key_here with your own API key.

The .env file is not included in the repository for security reasons.

5. Change git remote url to avoid accidental pushes to base project

```
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
```

### Required Packages

```
pip install os requests python-dotenv
```

## External Services

___

This project retrieves movie information using the api-ninjas.

API website: https://api-ninjas.com/


## **Running the Application**

___

Start the program:

```
python animals_web_generator.py
```

## **Usage**

___

### Example Workflow

1. User is asked to enter a name of an animal:

```
Enter a name of an animal:
```

2. A web page is created.

```
Website was successfully generated to the file animals.html.
```

3. The user is asked if he/she wants to create a website only for the animals with a particular skin type.

```
Do you want to create a website only for the animals with a particular skin type? (y/n) 
```

4. The user is asked to choose a skin type from a list of available skins:

```
Please choose a skin type: Hair, Fur, Scales 
```

5. A web page for the animals with the skin type entered by the user is created

```
Website was successfully generated to the file animal_hair.html.
```

## Acknowledgments

___

- Animals data provided by the API Ninjas.

## **Contact**

___

Ester Plaza Fernández - esterplaza@gmail.com

Project Link: https://github.com/esterplaza/Movie-Project.git

