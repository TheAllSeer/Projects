import datetime
myname = 'Itamar Barkai'
myage = 24
myDoB = datetime.datetime(1998, 2, 19)
myemail = 'ibark.bu@gmail.com'
myGit = 'https://github.com/TheAllSeer'
myLinked = 'https://www.linkedin.com/in/itamar-barkai-26119a226/'
myUpwork = 'https://www.upwork.com/freelancers/~01b87343c472baed1e'
coverletter = 'I know that the world is going to continue evolving into a more technology oriented area, where inevitably people will feel more lonely. social media is a powerful tool to combat this phenomenon, and I want to help make the situation better.'

header = {'name':myname,
            'age':myage,
            'DoB':myDoB,
            'email':myemail,
            'git':myGit,
            'linkedin':myLinked,
            'freelance':myUpwork,
            'cover':coverletter
}
about = "I am a passionate full-stack developer who specializes in Python. I am a quick learned looking to challenge myself by working on interesting and important projects. my emphasis is on the project's end goal more than the programming language I use."
projects = {'project1':{'title':'Facebook Marketplace Scraper',
                        'desc':"the scraper searches the marketplace for listings that match specific criteria such as price range, category, and keywords. Once it finds new listings that match these criteria, it sends an email notification to the user. This tool can be used to keep track of new listings that match specific criteria, such as products that fall within a certain price range or keywords that are relevant to your interests. This can be helpful for businesses or individuals who want to stay informed about new products or deals on the marketplace, or for tracking prices and inventory of certain products."}}
skills = {'skill1':{'title':'Programming Languages',
                    'desc':'Python, SQL, JavaScript, HTML, CSS, JSON'},
            'skill2':{'title':'Tools',
                    'desc':'Jupyter-lab, advanced Excel, Visual Studio Code, SSMS, Power BI'},
            'skill3':{'title':'languages',
                    'desc':'native speaker in both Hebrew and English'}
        }                 

exp = {'exp1':{'title':'Language Data Analyst',
                'company':'Transperfect',
                'time':f"from {datetime.datetime(2022, 8, 2)} until {datetime.datetime(2022, 12, 1)}"},
        'exp2':{'title':'Full Stack Developer',
                'company':'Freelance',
                'time':f"from {datetime.datetime(2022, 12, 2)} and going"}
}
edu = {'edu1':{'title':'High School Diploma',
                'institution':'Hebrew Reali School, Beit Biram',
                'desc':"full high school diploma"},
        'edu2':{'title':'Pre Academic Program',
                'institution':'Technion - Israeli Institute of Technology',
                'desc':"pre academic program with extensive physics and mathematics learning"},
        'edu3':{'title':'Psychometric exam',
                'institution':'Generalized National Test',
                'desc':"scored 664, with a mathematics oriented score of 682"},
}
hobbies = {'hobby1':{'title':'Gym',
                    'desc':'have been working out for 9 years and have participated in 5 national powerlifting competitions'},
            'hobby2':{'title':'Guitar',
                    'desc':"I've been playing guitar for the past 9 years"},
            'hobby3':{'title':'Gaming',
                    'desc':'I have been playing video games for the past 14 years'}
        }  

certs = {'cert1':{'alt':'Coursera WD4E complete course',
                    'src':'Coursera WD4E complete course.jpg'},
        'cert2':{'alt':'Coursera Computational thinking Penn',
                    'src':'Coursera Computational thinking Penn.jpg'}, 
        'cert3':{'alt':'John Bryce Data Analyst Expert',
                    'src':'John Bryce_page-0001.jpg'}           
                               
}
page_json ={'header':header,
            'about':about,
            'projects':projects,
            'skills':skills,
            'experience':exp,
            'education':edu,
            'certificates':certs,
            'hobbies':hobbies}



print(page_json)