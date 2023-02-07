const addSkill = document.querySelector('#add-skill');
addSkill.addEventListener('click', function (event) {
    event.preventDefault();
    const newSkillInput = addSkill.previousElementSibling.querySelector('input');
    if (newSkillInput.value.length === 0) {
        alert("Kindly Enter Skill Name!!!!");
    } else {
        const SkillsContainer = addSkill.parentElement;
        const newSkill = document.createElement("div");
        newSkill.classList.add("skill");
        newSkill.innerHTML = `<span class="skill-text"> ${newSkillInput.value} </span> <button class="delete"> <i class="far fa-trash-alt"></i> </button>`;
        newSkill.querySelector(".delete").addEventListener("click", function () {
            newSkill.remove();
        });
        SkillsContainer.appendChild(newSkill);
        newSkillInput.value = "";
    }
});