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