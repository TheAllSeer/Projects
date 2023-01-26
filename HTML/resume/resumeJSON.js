// for skills just to have an example of how it works
var xhr = new XMLHttpRequest();
xhr.open("GET", "resumeJSON.json", true);
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    var data = JSON.parse(xhr.responseText);
    var ss = data.skills;
    var os = Object.values(ss);
    var ulSkills = document.querySelector("section.skills>div.section-body>ul");
    os.forEach((s) => {
      let skillItem = document.createElement("li");
      skillItem.innerHTML = s.title + ": " + s.desc;
      ulSkills.appendChild(skillItem);
    });
  }
};
xhr.send();

// starting from the top. this is header:

var xhr = new XMLHttpRequest();
xhr.open("GET", "JSONresume.json", true);
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    var data = JSON.parse(xhr.responseText);

    var dobItem = document.createElement("li");
    dobItem.innerHTML =
      '<i class="fa-solid fa-calendar"></i>: ' + data.header.DoB; // DoB is case sensitive
    document.querySelector("ul.contact-info").appendChild(dobItem);
    var phoneItem = document.createElement("li");
    phoneItem.innerHTML =
      '<i class="fa-solid fa-phone"></i>: ' + data.header.phone;
    document.querySelector("ul.contact-info").appendChild(phoneItem);

    var mailItem = document.createElement("li");
    mailItem.innerHTML = '<i class="fa-solid fa-at"></i>: ' + data.header.email;
    document.querySelector("ul.contact-info").appendChild(mailItem);

    var gitItem = document.createElement("li");
    gitItem.innerHTML =
      '<i class="fa-brands fa-github"></i>: ' + data.header.git;
    document.querySelector("ul.contact-info").appendChild(gitItem);

    var liItem = document.createElement("li");
    liItem.innerHTML =
      '<i class="fa-brands fa-linkedin"></i>: ' + data.header.linkedin;
    document.querySelector("ul.contact-info").appendChild(liItem);

    var flItem = document.createElement("li");
    flItem.innerHTML =
      '<i class="fa-brands fa-python"></i>: ' + data.header.freelance;
    document.querySelector("ul.contact-info").appendChild(flItem);

    var name = document.querySelector("div.name");
    name.innerHTML = data.name;

    var coverLetterText = document.querySelector(".cover-letter>.section-body");
    coverLetterText.innerHTML = data.coverLetter;

    var aboutText = document.querySelector(".about>.section-body");
    aboutText.innerHTML = data.about;

    var projectsList = document.querySelector("ul.projects-ul");
    projectsData = data.projects;
    projectsDataObject = Object.values(projectsData);
    projectsDataObject.forEach((o) => {
      listItem = document.createElement("li");
      title = o.title;
      desc = o.desc;
      titleItem = document.createElement("h3");
      titleItem.innerHTML = title;
      listItem.appendChild(titleItem);
      descItem = document.createElement("p");
      descItem.innerHTML = desc;
      listItem.appendChild(descItem);
      projectsList.appendChild(listItem);
    });

    var skillsList = document.querySelector("ul.skills-ul");
    skillsData = data.skills;
    skillsDataObject = Object.values(skillsData);
    skillsDataObject.forEach((o) => {
      listItem = document.createElement("li");
      title = o.title;
      desc = o.desc;
      titleItem = document.createElement("h3");
      titleItem.innerHTML = title;
      listItem.appendChild(titleItem);
      descItem = document.createElement("p");
      descItem.innerHTML = desc;
      listItem.appendChild(descItem);
      skillsList.appendChild(listItem);
    });

    var expList = document.querySelector(".exp-ul");
    expData = data.experience;
    expDataO = Object.values(expData);
    expDataO.forEach((o) => {
      listItem = document.createElement("li");
      title = o.title;
      company = o.company;
      time = o.time;
      titleItem = document.createElement("h4");
      titleItem.innerHTML = title;
      listItem.appendChild(titleItem);
      companyItem = document.createElement("h5");
      companyItem.innerHTML = company;
      listItem.appendChild(companyItem);
      timeItem = document.createElement("p");
      timeItem.innerHTML = time;
      listItem.appendChild(timeItem);
      expList.appendChild(listItem);
    });

    var eduUL = document.querySelector("ul.edu-ul");
    eduData = data.education;
    eduDataObject = Object.values(eduData);
    eduDataObject.forEach((o) => {
      listItem = document.createElement("li");
      h4Item = document.createElement("h4");
      h4Item.innerHTML = o.title + " - " + o.institution;
      listItem.appendChild(h4Item);
      listItem.append(o.desc);
      eduUL.appendChild(listItem);
    });
    var hobbiesUL = document.querySelector(".hobbies-ul");
    hobbiesData = data.hobbies;
    hobbiesDataObject = Object.values(hobbiesData);
    hobbiesDataObject.forEach((o) => {
      listItem = document.createElement("li");
      listItem.innerHTML = "<h3>" + o.title + "</h3> " + o.desc;
      hobbiesUL.appendChild(listItem);
    });

    var certsDiv = document.querySelector("div.certs-body");
    certs = data.certificates;
    certsO = Object.values(certs);
    certsO.forEach((o) => {
      imge = document.createElement("img");
      imge.src = o.src;
      imge.alt = o.alt;
      imge.style = "width:25rem;";
      certsDiv.appendChild(imge);
    });
  }
};
xhr.send();
