document.getElementById("submit-form").addEventListener("click", function(event) {
   // Execute your JavaScript code here
   var forms = document.getElementById("forms");
   forms.classList.remove("form");
   forms.innerHTML = '<div class="welcome"><div class="content"><svg class="checkmark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 52 52"><circle class="checkmark__circle" cx="26" cy="26" r="25" fill="none"/><path class="checkmark__check" fill="none" d="M14.1 27.2l7.1 7.2 16.7-16.8"/></svg><h2>Thanks for Feedback!</h2><div></div>';

   // Now, submit the form
   var formsElement = document.getElementById("forms");
   var formData = new FormData(formsElement);
   fetch(formsElement.action, {
     method: 'POST',
     body: formData,
     headers: {
       'X-CSRFToken': "{{ csrf_token }}", // Add CSRF token if needed
     }
   })
   .then(response => {
     // Handle the response or perform additional actions if needed
   })
   .catch(error => {
     // Handle errors
   });

   event.preventDefault(); // Prevent default form submission behavior
 });