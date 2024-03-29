import json

# this is the file to control the data inside the json file. 
# do not touch the file JSONresume.json manually, only modify it HERE!



data = {}
data = {
    "name":"Itamar Barkai",
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
data['about'] = "I am a passionate full-stack developer who specializes in Python. I am a quick learned looking to challenge myself by working on interesting and important projects. my emphasis is on the project's end goal more than the programming language I use."

data['projects'] = {
    0:{
      "title": "Facebook Marketplace Scraper",
      "desc": "the scraper searches the marketplace for listings that match specific criteria such as price range, category, and keywords. Once it finds new listings that match these criteria, it sends an email notification to the user. This tool can be used to keep track of new listings that match specific criteria, such as products that fall within a certain price range or keywords that are relevant to your interests. This can be helpful for businesses or individuals who want to stay informed about new products or deals on the marketplace, or for tracking prices and inventory of certain products."
    }
}

data["skills"]={
    0: {
      "title": "Programming Languages",
      "desc": "Python, SQL, JavaScript, HTML, CSS, JSON"
    },
    1: {
      "title": "Tools",
      "desc": "Jupyter-lab, advanced Excel, Visual Studio Code, SSMS, Power BI"
    },
    2: {
      "title": "languages",
      "desc": "native speaker in both Hebrew and English"
    }
  }

data["experience"] = {
    0: {
      "title": "Language Data Analyst",
      "company": "Transperfect",
      "time": "from 2022-08-02 until 2022-12-01"
    },
    1: {
      "title": "Full Stack Developer",
      "company": "Freelance",
      "time": "from 2022-12-02 and going"
    }
  }
data["education"]= {
    0: {
      "title": "High School Diploma",
      "institution": "Hebrew Reali School, Beit Biram",
      "desc": "full high school diploma"
    },
    1: {
      "title": "Pre Academic Program",
      "institution": "Technion - Israeli Institute of Technology",
      "desc": "pre academic program with extensive physics and mathematics learning"
    },
    2: {
      "title": "Psychometric exam",
      "institution": "Generalized National Test",
      "desc": "scored 664, with a mathematics oriented score of 682"
    }
  }


data["certificates"]= {
    "cert1": {
      "alt": "Coursera WD4E complete course",
      "src": "Coursera WD4E complete course.jpg"
    },
    "cert2": {
      "alt": "Coursera Computational thinking Penn",
      "src": "Coursera Computational thinking Penn.jpg"
    },
    "cert3": {
      "alt": "John Bryce Data Analyst Expert",
      "src": "John Bryce_page-0001.jpg"
    }
  }


data["hobbies"]= {
    "hobby1": {
      "title": "Gym",
      "desc": "have been working out for 9 years and have participated in 5 national powerlifting competitions"
    },
    "hobby2": {
      "title": "Guitar",
      "desc": "I've been playing guitar for the past 9 years"
    },
    "hobby3": {
      "title": "Gaming",
      "desc": "I have been playing video games for the past 14 years"
    }
  }
data['coverLetter'] = 'I know that the world is going to continue evolving into a more technology oriented area, where inevitably people will feel more lonely. social media is a powerful tool to combat this phenomenon, and I want to help make the situation better.'
print(json.dumps(data, indent=4))
with open('JSONresume.json', 'w') as file:
    json.dump(data, file)
