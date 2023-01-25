const fs = require("fs");
var jsonData = JSON.parse(fs.readFileSync("resumeJSON.json", "utf8"));

var ss = jsonData.skills;
var os = Object.values(ss);
os.forEach((s) => {
  console.log(s.title, s.desc);
});

var ulSkills = querySelector("section.skills>div.section-body>ul");
os.forEach((s) => {
  let skillItem = createElement("li");
  skillItem.innerHTML = s.title + ": " + s.desc;
  ulSkills.appendChild(skillItem);
});
