// Define the input functions

/**
 * Validates the name input field.
 * Checks for empty, and if it contains both first and last names.
 * Displays appropriate error messages.
 * @returns {boolean} - True if the name is valid, false otherwise.
 */
function validateName() {
    // Get the span for displaying name errors by their IDs
    let nameError = document.getElementById("name-error");
    // Get the value of the name input
    let name = document.getElementById("fullname").value;
    
    // Check if the input is empty
    if (name.length === 0) {
        nameError.innerHTML = "Name is required";
        return false;
    }

    // Check if the input contains both first and last names
    if (!name.match(/^[A-Za-z]+ [A-Za-z]+$/)) {
        nameError.innerHTML = "Please write your full name";
        return false;
    }
    // If the input is valid, display a validation symbol
    nameError.innerHTML = '<img src="/static//Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

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
 * Validates the phone input field.
 * Checks for empty and a valid 10-digit phone number format.
 * Displays appropriate error messages.
 * @returns {boolean} - True if the phone is valid, false otherwise.
 */
function validatePhone() {
    let phoneError = document.getElementById("phone-error");
    // Get the value of the phone input
    let phone = document.getElementById("phone").value;
    
    // Check if the input is empty
    if (phone.length === 0) {
        phoneError.innerHTML = "Phone is required";
        return false;
    }

    // Check if the input matches a valid 10-digit phone number format
    if (!phone.match(/^\d{10}$/)) {
        // Display an error message in the error element
        phoneError.innerHTML = 'Please enter a valid phone number.';
        return false;
    }
    // If the input is valid, display a validation symbol
    phoneError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

/**
 * Validates the password input field.
 * Checks for empty and a valid password format.
 * Displays appropriate error messages.
 * @returns {boolean} - True if the password is valid, false otherwise.
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
 * Validates the password confirmation input field.
 * Checks for empty and if it matches the password.
 * Displays appropriate error messages.
 * @returns {boolean} - True if the confirmation matches the password, false otherwise.
 */
function validateConfirm() {
    let confirmError = document.getElementById("confirm-error");
    // Get the value of the confirmation input
    let confirm = document.getElementById("password").value;
    
    // Check if the input is empty
    if (confirm.length === 0) {
        confirmError.innerHTML = "Confirm Password is required";
        return false;
    }

    // Check if the input matches the password
    if (confirm !== document.getElementById("confirm_password").value) {
        // Display an error message in the error element
        confirmError.innerHTML = 'Passwords do not match.';
        return false;
    }
    // If the input is valid, display a validation symbol
    confirmError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

/**
 * Validates the entire signup form.
 * Checks all fields for correctness and completeness.
 * Displays an error message if any field is empty or invalid.
 * @returns {boolean} - True if the form is valid, false otherwise.
 */
function validateForm() {
    // Get the span for displaying form errors
    let signupError = document.getElementById("signup-error");

    // Check if any of the fields are empty or invalid
    if (!validateName() || !validateEmail() || !validatePhone() || !validatePassword() || !validateConfirm()) {
        // Display an error message in the error element
        signupError.style.display = "block";
        signupError.innerHTML = "Please fill all fields correctly";
        
        // Hide form errors after 3 seconds
        setTimeout(() => { signupError.style.display = "none" }, 3000);

        return false;
    }
    return true;
}