document.getElementById("feedback-form").addEventListener("submit", function(e) {
    // Prevent default form submission behavior
    e.preventDefault();

    // Perform validations
    if (validateForm()) {
        // If all checks pass, submit the form
        e.target.submit();
    }
});

function validateForm() {
    // Full Name Validation
    const fullName = document.getElementById("full-name").value;
    if (!fullName) {
        alert("Full Name is required.");
        return false;
    }

    // Email Validation
    const email = document.getElementById("email").value;
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Phone Number Validation
    const phone = document.getElementById("phone").value;
    const phonePattern = /^\d{10}$/;  // Simple 10-digit check
    if (!phonePattern.test(phone)) {
        alert("Please enter a valid 10-digit phone number.");
        return false;
    }

    // Purchase Date Validation
    const purchaseDate = new Date(document.getElementById("purchase-date").value);
    const currentDate = new Date();
    if (purchaseDate > currentDate) {
        alert("Purchase date cannot be in the future.");
        return false;
    }

    // Feedback Length Validation (if you have fields for likes, dislikes, and comments)
    const likes = document.getElementsByName("likes")[0].value;
    const dislikes = document.getElementsByName("dislikes")[0].value;
    const comments = document.getElementsByName("comments")[0].value;

    if (likes.length > 500 || dislikes.length > 500 || comments.length > 500) {
        alert("Feedback fields cannot exceed 500 characters.");
        return false;
    }

    // If everything is valid
    return true;
}
