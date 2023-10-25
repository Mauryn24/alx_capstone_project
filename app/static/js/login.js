// Define the input functions

/**
 * Validates the email input field.
 * Checks for empty and valid email format.
 * Displays appropriate error messages.
 * @returns {boolean} - True if email is valid, false otherwise.
 */
function validateEmail() {
    let emailError = document.getElementById("email-error");
    // Get the value of the email input
    let email = document.getElementById("email").value;

    // Check if the input is empty
    if (email.length === 0) {
        emailError.innerHTML = "Email is required";
        return false;
    }

    // Check if the input matches a valid email format
    if (!email.match(/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/)) {
        // Display an error message in the error element
        emailError.innerHTML = 'Please enter a valid email address.';
        return false;
    }
    // If the input is valid, display a validation symbol
    emailError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

/**
 * Validates the password input field.
 * Checks for empty and valid password format.
 * Displays appropriate error messages.
 * @returns {boolean} - True if password is valid, false otherwise.
 */
function validatePassword() {
    let passwordError = document.getElementById("password-error");
    // Get the value of the password input
    let password = document.getElementById("password").value;

    // Check if the input is empty
    if (password.length === 0) {
        passwordError.innerHTML = "Password is required";
        return false;
    }

    // Check if the input matches a valid password format
    if (!password.match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/)) {
        // Display an error message in the error element
        passwordError.innerHTML = 'Please enter a valid password.';
        return false;
    }
    // If the input is valid, display a validation symbol
    passwordError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

/**
 * Validates the entire form, checking both email and password inputs.
 * Displays an error message if any field is empty or invalid.
 * @returns {boolean} - True if the form is valid, false otherwise.
 */
function validateForm() {
    // Get the span for displaying form errors
    let signupError = document.getElementById("signup-error");

    // Check if any of the fields are empty or invalid
    if (!validateEmail() || !validatePassword()) {
        // Display an error message in the error element
        signupError.style.display = "block";
        signupError.innerHTML = "Please fill all fields correctly";

        // Hide form errors after 3 seconds
        setTimeout(() => { signupError.style.display = "none" }, 3000);

        return false;
    }
    return true;
}