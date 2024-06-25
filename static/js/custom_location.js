document.addEventListener("DOMContentLoaded", function() {
    const locationSelect = document.getElementById("id_location");
    const customLocationInput = document.getElementById("id_custom_location");
    
    function toggleCustomLocation() {
        if (locationSelect.value === "Others") {
            customLocationInput.parentElement.style.display = "block";
        } else {
            customLocationInput.parentElement.style.display = "none";
            customLocationInput.value = "";
        }
    }
    locationSelect.addEventListener("change", toggleCustomLocation);
    toggleCustomLocation();
});