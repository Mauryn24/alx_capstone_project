// Define the input functions

// Name
function validateName() {
    // get the span errors by their ids
    let nameError = document.getElementById("name-error");
    // takes value of input
    let name = document.getElementById("username").value;
    // checks if input is empty
    if (name.length === 0) {
        nameError.innerHTML = "Name is required";
        return false;
    }
    // checks if the input field has both names and spaces
    if(!name.match(/^[A-Za-z]+ [A-Za-z]+$/)) {
        nameError.innerHTML = "write full name";
        return false;
    }
    // if input is valid
    nameError.innerHTML = '<img src="/static//Pictures/valid.png" alt="tick" width="20px">';
    return true;
    
}

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
    if(!email.match(/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/)) {
        // Display an error message in the error element
        emailError.innerHTML = 'Please enter a valid email address.';
        // // Return false to prevent form submission
        return false;
    }
    // if input is valid
    emailError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

// Phone
function validatePhone() {
    let phoneError = document.getElementById("phone-error");
    // takes value of input
    let phone = document.getElementById("phone").value;
    
    // checks if input is empty
    if (phone.length === 0) {
        phoneError.innerHTML = "Phone is required";
        return false;
    }
    
    // checks if input is valid
    if(!phone.match(/^\d{10}$/)) {
        // Display an error message in the error element
        phoneError.innerHTML = 'Please enter a valid phone number.';
        // // Return false to prevent form submission
        return false;
    }
    // if input is valid
    phoneError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
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
    if(!password.match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/)) {
        // Display an error message in the error element
        passwordError.innerHTML = 'Please enter a valid password.';
        // // Return false to prevent form submission
        return false;
    }
    // if input is valid
    passwordError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

// Confirm Password
function validateConfirm() {
    let confirmError = document.getElementById("confirm-error");
    // takes value of input
    let confirm = document.getElementById("confirm").value;
    
    // checks if input is empty
    if (confirm.length === 0) {
        confirmError.innerHTML = "Confirm Password is required";
        return false;
    }
    
    // checks if input is valid
    if(confirm !== document.getElementById("password").value) {
        // Display an error message in the error element
        confirmError.innerHTML = 'Passwords do not match.';
        // // Return false to prevent form submission
        return false;
    }
    // if input is valid
    confirmError.innerHTML = '<img src="/static/Pictures/valid.png" alt="tick" width="20px">';
    return true;
}

// Submit
function validateForm() {
    // get the span Errors
    let signupError = document.getElementById("signup-error");

    // check if any of the fields are empty or invalid
    if (!validateName() || !validateEmail() || !validatePhone() || !validatePassword() || !validateConfirm()) {
        // Display an error message in the error element
        signupError.style.display = "block";
        // Return false to prevent form submission
        signupError.innerHTML = "Please fill all fields correctly";
        // hides form errors after 3 seconds
        setTimeout(() => { signupError.style.display = "none"}, 3000);
            return false;
        }
    }
