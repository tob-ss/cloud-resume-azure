// Counter.js - Visitor counter functionality for Azure Resume Challenge

document.addEventListener('DOMContentLoaded', function() {
    // Get the counter element
    const counterElement = document.getElementById('counter');
    
    // Add loading indicator
    counterElement.innerHTML = '<span class="counter-loading"></span>';

    // Determine environment dynamically
    const isDev = window.location.hostname.includes('dev') || 
                 // window.location.hostname.includes('localhost');
                  window.location.hostname.includes('jwmugt4mm4bwe');

    // Set the appropriate API base URL
    const apiBaseUrl = isDev 
        ? 'https://resume-func-dev-jwmugt4mm4bwe.azurewebsites.net/api/'
        : 'https://resume-func-prd-s4ot3manh2e7g.azurewebsites.net/api/'

    const getResumeUrl = `${apiBaseUrl}GetResumeCounter`;
    const updateResumeUrl = `${apiBaseUrl}UpdateResumeCounter`;
        
    // Function to get the counter value from the API
    async function getCount() {
        try {
            
            // API URL - update this with your Azure Function URL
            // For local testing, you can use:
            //const apiUrl = 'http://localhost:7071/api/GetResumeCounter';
            
            // Fetch the counter value
            const response = await fetch(getResumeUrl);
            
            // Check if the response is ok
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            
            // Parse the JSON response
            const data = await response.json();
            
            // Update the counter with the value
            counterElement.textContent = data.count;
            
            // Update the counter by calling the UpdateResumeCounter function
            updateCount();
            
        } catch (error) {
            console.error('Error fetching visitor count:', error);
            counterElement.textContent = 'Unable to load visitor count';
        }
    }
    
    // Function to update the counter
    async function updateCount() {
        try {
            // API URL - update this with your Azure Function URL
            //const apiUrl = 'https://resume-func-dev-jwmugt4mm4bwe.azurewebsites.net/api/UpdateResumeCounter?';
            
            // For local testing, you can use:
            //const apiUrl = 'http://localhost:7071/api/UpdateResumeCounter';
            
            // Call the update function
            const response = await fetch(updateResumeUrl);
            
            // Check if the response is ok
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            
            // Parse the JSON response
            const data = await response.json();
            
            // Update the counter with the updated value
            counterElement.textContent = data.count;
            
        } catch (error) {
            console.error('Error updating visitor count:', error);
            // We already have the retrieved count, so no need to show an error
        }
    }
    
    // Call the getCount function to initialize
    getCount();
});