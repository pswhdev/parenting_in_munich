/**
 * Displays a preview of the selected profile photo.
 * This function is triggered when a user selects a new photo file.
 * It reads the file using FileReader (a built-in JavaScript object 
 * provided by the browser's File API that allows web applications
 * to read the contents of files and sets the preview image source to
 * the selected file.
 */
function displayProfilePhotoPreview(event) {
    // Create a new FileReader object to read the selected file
    const fileReader = new FileReader();
    
    // Define the onload event handler (fires when the file is fully read) for the FileReader
    fileReader.onload = function() {
        // Get the img element for the profile photo preview
        const profilePhotoPreview = document.getElementById('profile-photo-preview');
        // Set the src of the img element to the result from FileReader
        profilePhotoPreview.src = fileReader.result;
        // Ensure the img element is visible
        profilePhotoPreview.style.display = 'block';
    }

    // Reads the file and triggers the onload event when done.
    fileReader.readAsDataURL(event.target.files[0]);

}