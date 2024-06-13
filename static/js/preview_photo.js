/**
 * Function called when user selects a new profile photo file.
 * It reads the selected file and displays a preview of the new photo.
 */
function displayProfilePhotoPreview(event) {

    const file = event.target.files[0];
        // Check for file size greater than 2MB
        if (file && file.size > 2 * 1024 * 1024) {
            // Show the modal
            var myModal = new bootstrap.Modal(document.getElementById('fileSizeModal'), {
                keyboard: false
            });
            myModal.show();
            event.target.value = "";
            return;
        }
        
    // Create a new FileReader object (API provided by web browsers to 
    // read the contents of files stored on the user's computer) to read the selected file
    const fileReader = new FileReader();
    
    // Once the file is fully read it runs the function
    fileReader.onload = function() {
        // Get the img element that will display the profile photo preview
        const profilePhotoPreview = document.getElementById('profile-photo-preview');
        
        // Set the src attribute of the img element to the file's data URL
        // This data URL is created by the FileReader and contains the file's contents
        profilePhotoPreview.src = fileReader.result;
        
        // Make sure the img element is visible (in case it was hidden)
        profilePhotoPreview.style.display = 'block';
        
        // Uncheck the delete photo checkbox because a new photo is selected
        document.getElementById('delete-photo-checkbox').checked = false;
    }

    // Read the selected file as a Data URL (base64 encoded string)
    // This will trigger the onload event handler when finished reading
    fileReader.readAsDataURL(event.target.files[0]);
}

/**
 * This function is called when the delete photo checkbox is checked or unchecked.
 * It updates the profile photo preview based on the checkbox state:
 * - If checked, the preview shows a default photo.
 * - If unchecked and a new file is selected, the preview shows the new file.
 * - If unchecked and no new file is selected, the preview shows the current photo.
 */
function handleDeletePhoto() {
    // Get references to the checkbox, profile photo preview, and file input elements
    const deletePhotoCheckbox = document.getElementById('delete-photo-checkbox');
    const profilePhotoPreview = document.getElementById('profile-photo-preview');
    const newPhotoInput = document.getElementById('id_profile_photo');

    if (deletePhotoCheckbox.checked) {
        // If the checkbox is checked, show the default photo
        profilePhotoPreview.src = defaultPhotoUrl;
    } else {
        // If the checkbox is unchecked
        if (newPhotoInput.files && newPhotoInput.files[0]) {
            // If there is a new file selected, read and display it.
            // newPhotoInput.files is a reference to the file input element (<input type="file" ...>).
            // it ensures that the file input element actually supports file selection.
            // .files[0] ensures at least one file has been selected (the .files property is a
            // FileList object representing the list of files selected by the user.)
            const fileReader = new FileReader();
            fileReader.onload = function() {
                // Set the src attribute of the img element to the file's data URL
                profilePhotoPreview.src = fileReader.result;
            }
            // Read the selected file as a Data URL
            fileReader.readAsDataURL(newPhotoInput.files[0]);
        } else {
            // If no new file is selected, show the current photo
            profilePhotoPreview.src = currentPhotoUrl;
        }
    }
}
