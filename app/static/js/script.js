// Get references to the buttons and sections
const changePasswordButton = document.getElementById('change-password-button');
const activityGoalsButton = document.getElementById('activity-goals-button');
const userInfoButton = document.getElementById('user-info-button');
const changePasswordSection = document.getElementById('change-password-section');
const activityGoalsSection = document.getElementById('activity-goals-section');
const userInfoSection = document.getElementById('user-info-section');

/**
 * Function to show a specific section and hide others
 * @param {HTMLElement} section - The section to be shown.
 */
function showSection(section) {
    // Hide all sections
    changePasswordSection.classList.add('hidden');
    activityGoalsSection.classList.add('hidden');
    userInfoSection.classList.add('hidden');

    // Show the selected section
    section.classList.remove('hidden');
}

// Add click event listeners to the buttons

/**
 * Event listener for the 'Change Password' button click
 */
changePasswordButton.addEventListener('click', () => showSection(changePasswordSection));

/**
 * Event listener for the 'Activity Goals' button click
 */
activityGoalsButton.addEventListener('click', () => showSection(activityGoalsSection));

/**
 * Event listener for the 'User Info' button click
 */
userInfoButton.addEventListener('click', () => showSection(userInfoSection));


// var data = {{ data| tojson | safe }};

// // Extract dates and workout sets from the data
// var dates = data.map(item => item.date);
// var workoutSets = data.map(item => item.sets);

// var ctx = document.getElementById('myChart').getContext('2d');
// var myChart = new Chart(ctx, {
//     type: 'bar',
//     data: {
//         labels: dates,
//         datasets: [{
//             label: 'Workout Sets',
//             data: workoutSets,
//             backgroundColor: 'rgba(75, 192, 192, 0.2)',
//             borderColor: 'rgba(75, 192, 192, 1)',
//             borderWidth: 1
//         }]
//     },
//     options: {
//         scales: {
//             x: {
//                 title: {
//                     display: true,
//                     text: 'Date'
//                 }
//             },
//             y: {
//                 title: {
//                     display: true,
//                     text: 'Workout Sets'
//                 },
//                 beginAtZero: true
//             }
//         }
//     }
// });

// Place this code inside your script.js file

// Function to initialize the chart
// function initializeChart(data) {
//     var dates = data.map(item => item.date);
//     var workoutSets = data.map(item => item.sets);

//     var ctx = document.getElementById('myChart').getContext('2d');
//     var myChart = new Chart(ctx, {
//         type: 'bar',
//         data: {
//             labels: dates,
//             datasets: [{
//                 label: 'Workout Sets',
//                 data: workoutSets,
//                 backgroundColor: 'rgba(75, 192, 192, 0.2)',
//                 borderColor: 'rgba(75, 192, 192, 1)',
//                 borderWidth: 1
//             }]
//         },
//         options: {
//             scales: {
//                 x: {
//                     title: {
//                         display: true,
//                         text: 'Date'
//                     }
//                 },
//                 y: {
//                     title: {
//                         display: true,
//                         text: 'Workout Sets'
//                     },
//                     beginAtZero: true
//                 }
//             }
//         }
//     });
// }

// // Fetch data from Flask route and initialize the chart
// fetch('/index/data/')
//     .then(response => response.json())
//     .then(data => initializeChart(data));

// Function to initialize the chart
// function initializeChart(data) {
//     var dates = data.map(item => item.date);
//     var workoutSets = data.map(item => item.sets);

//     var ctx = document.getElementById('myChart').getContext('2d');
//     var myChart = new Chart(ctx, {
//         type: 'bar',
//         data: {
//             labels: dates,
//             datasets: [{
//                 label: 'Workout Sets',
//                 data: workoutSets,
//                 backgroundColor: 'rgba(75, 192, 192, 0.2)',
//                 borderColor: 'rgba(75, 192, 192, 1)',
//                 borderWidth: 1
//             }]
//         },
//         options: {
//             scales: {
//                 x: {
//                     title: {
//                         display: true,
//                         text: 'Date'
//                     }
//                 },
//                 y: {
//                     title: {
//                         display: true,
//                         text: 'Workout Sets'
//                     },
//                     beginAtZero: true
//                 }
//             }
//         }
//     });
// }

// // Fetch data from Flask route and initialize the chart
// fetch('/index/data')
//     .then(response => response.json())
//     .then(data => initializeChart(data));