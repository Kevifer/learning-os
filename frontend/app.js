async function loadGoals() {
    const response = await fetch("http://127.0.0.1:8000/goals");

    const goals = await response.json();

    const goalsContainer = document.getElementById("goals");

    goalsContainer.innerHTML = "";

    goals.forEach(goal => {
        const goalElement = document.createElement("div");

        goalElement.innerHTML = `
            <h3>${goal.name}</h3>
            <p>${goal.description ?? ""}</p>
        `;

        goalsContainer.appendChild(goalElement);
    });
}

    const goalForm = document.getElementById("goal-form");


    goalForm.addEventListener("submit", async event => {

      event.preventDefault();
        const name = document.getElementById("goal-name").value;
        const description = document.getElementById("goal-description").value;

    });

loadGoals();
	
