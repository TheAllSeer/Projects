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
  }
};
xhr.send();
