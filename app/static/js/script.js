// Function to add a new workout
function addWorkout(event) {
    event.preventDefault();

    // Fetch data from the form fields
    const exercise = document.getElementById("exercise").value;
    const sets = document.getElementById("sets").value;
    const reps = document.getElementById("reps").value;
    const duration = document.getElementById("duration").value;
    const date = new Date().toLocaleDateString(); // Get the current date

    const workout = {
        exercise: exercise,
        sets: sets,
        reps: reps,
        duration: duration,
        date: date // Include the date
    };

    // Retrieve the existing workout history from localStorage (if it exists)
    let workoutHistory = JSON.parse(localStorage.getItem("workoutHistory")) || [];

    // Add the new workout to the history
    workoutHistory.push(workout);

    // Store the updated history back in localStorage
    localStorage.setItem("workoutHistory", JSON.stringify(workoutHistory));

    // Update the UI
    updateWorkoutHistory(workoutHistory);

    // Clear the form fields
    document.getElementById("exercise").value = "";
    document.getElementById("sets").value = "";
    document.getElementById("reps").value = "";
    document.getElementById("duration").value = "";
}

function updateWorkoutHistory(workoutHistory) {
    const workoutList = document.getElementById("workout-list");
    workoutList.innerHTML = ""; // Clear the existing list

    workoutHistory.forEach((workout, index) => {
        const workoutItem = document.createElement("li");
        workoutItem.innerHTML = `Date: ${workout.date}, Exercise: ${workout.exercise}, Sets: ${workout.sets}, Reps: ${workout.reps}, Duration: ${workout.duration} minutes <button class="edit-workout">Edit</button> <button class="delete-workout" data-index="${index}">Delete</button>`;
        workoutList.appendChild(workoutItem);

        workoutItem.querySelector(".delete-workout").addEventListener("click", deleteWorkout);
        workoutItem.querySelector(".edit-workout").addEventListener("click", () => editWorkout(index, workoutHistory));
    });
}