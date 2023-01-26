import json

# this is the file to control the data inside the json file. 
# do not touch the file JSONresume.json manually, only modify it HERE!



data = {}
data = {
  "header": {
    "name": "Itamar Barkai",
    "age": 24,
    "DoB": "1998-02-19",
    "email": "ibark.bu@gmail.com",
    "phone": "+972 - 52 - 641 - 2626",
    "git": "https://github.com/TheAllSeer",
    "linkedin": "https://www.linkedin.com/in/itamar-barkai-26119a226/",
    "freelance": "https://www.upwork.com/freelancers/~01b87343c472baed1e",
    "cover": "I know that the world is going to continue evolving into a more technology oriented area, where inevitably people will feel more lonely. social media is a powerful tool to combat this phenomenon, and I want to help make the situation better."
  }
}





with open('JSONresume.json', 'w') as file:
    json.dump(data, file)
