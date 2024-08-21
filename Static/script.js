document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();
    console.log("Form submitted!");

    // Hide the upload form and show the loading screen
    document.getElementById('upload-form-section').style.display = 'none';
    document.getElementById('loading-screen').style.display = 'block';
    console.log("Loading screen should be visible now.");

    const formData = new FormData();
    const fileInput = document.getElementById('file-input');
    formData.append('file', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        console.log('Response received, checking if JSON:', response);
        return response.json();  // Parse the JSON from the response
    })
    .then(data => {
        console.log('Parsed JSON:', data);
        if (data.error) {
            alert(data.error);
            document.getElementById('loading-screen').style.display = 'none';
            document.getElementById('upload-form-section').style.display = 'block';
        } else {
            console.log('File uploaded successfully:', data.filename);
            // Here, you would handle the display of the transcript and summary
            document.getElementById('loading-screen').style.display = 'none';
            
            // Inject the transcript and summary into the summary section
            document.getElementById('summary-section').innerHTML = `
                <h2>Transcript:</h2>
                <p>${data.transcription}</p>
                <h2>Summary:</h2>
                <p>${data.summary}</p>
            `;
            
            // Make sure the summary section is visible
            document.getElementById('summary-section').style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Error occurred:', error);
        document.getElementById('loading-screen').style.display = 'none';
        document.getElementById('upload-form-section').style.display = 'block';
    });
});
