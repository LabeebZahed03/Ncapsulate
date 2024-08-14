document.getElementById('upload-form').addEventListener('submit',function(event){
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('file-input');
    formData.append('file', fileInput.files[0]);
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert('File uploaded successfully: ' + data.filename);
            // Optionally redirect to another page or display the summary
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});