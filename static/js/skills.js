const addButtons = document.querySelectorAll('.add');
addButtons.forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault();
        const newTaskInput = button.previousElementSibling.querySelector('input');
        if (newTaskInput.value.length === 0) {
            alert("Kindly Enter Task Name!!!!");
        } else {
            const tasksContainer = button.parentElement;
            const newTask = document.createElement("div");
            newTask.classList.add("task");
            newTask.innerHTML = `<span class="taskname"> ${newTaskInput.value} </span> <button class="delete"> <i class="far fa-trash-alt"></i> </button>`;
            newTask.querySelector(".delete").addEventListener("click", function () {
                newTask.remove();
            });
            tasksContainer.appendChild(newTask);
            newTaskInput.value = "";
        }
    });
});