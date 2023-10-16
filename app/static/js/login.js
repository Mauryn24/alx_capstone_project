// Define the input functions

// Email
function validateEmail() {
    let emailError = document.getElementById("email-error");
    // takes value of input
    let email = document.getElementById("email").value;

    // checks if input is empty
    if (email.length === 0) {
        emailError.innerHTML = "Email is required";
        return false;
    }

    // checks if input is valid
    if (!email.match(/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/)) {
        // Display an error message in the error element
        emailError.innerHTML = 'Please enter a valid email address.';
        // // Return false to prevent form submission
        return false;
    }
    // if input is valid
    emailError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

// Password
function validatePassword() {
    let passwordError = document.getElementById("password-error");
    // takes value of input
    let password = document.getElementById("password").value;

    // checks if input is empty
    if (password.length === 0) {
        passwordError.innerHTML = "Password is required";
        return false;
    }

    // checks if input is valid
    if (!password.match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/)) {
        // Display an error message in the error element
        passwordError.innerHTML = 'Please enter a valid password.';
        // // Return false to prevent form submission
        return false;
    }
    // if input is valid
    passwordError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

// submit
function validateForm() {
    // get the span Errors
    let signupError = document.getElementById("signup-error");

    // check if any of the fields are empty or invalid
    if (!validateEmail() || !validatePassword()) {
        // Display an error message in the error element
        signupError.style.display = "block";
        // Return false to prevent form submission
        signupError.innerHTML = "Please fill all fields correctly";
        // hides form errors after 3 seconds
        setTimeout(() => { signupError.style.display = "none"}, 3000);
            return false;
        }
    }