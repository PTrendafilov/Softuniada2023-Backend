const addResponsibility = document.querySelector('#add-responsibility');
addResponsibility.addEventListener('click', function(ev) {
    ev.preventDefault();
    const newResponsibilityInput = document.querySelector('#responsibility-textarea');
    if (newResponsibilityInput.value.length === 0) {
        alert("Kindly Enter Responsibility!!!!");
    }else{
        const responsibitiesContainer = addResponsibility.parentElement;
        console.log(responsibitiesContainer)
        const newResponsibility = document.createElement("div");
        newResponsibility.classList.add("responsibility");
        newResponsibility.innerHTML = `<span class="responsibility-text"> ${newResponsibilityInput.value} </span> <button class="delete"> <i class="far fa-trash-alt"></i> </button>`;
        newResponsibility.querySelector(".delete").addEventListener("click", function () {
            newResponsibility.remove();
        });
        responsibitiesContainer.appendChild(newResponsibility);
        newResponsibilityInput.value = "";
    }
});