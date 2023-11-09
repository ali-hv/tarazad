function uploadAvatar() {
  var form = document.getElementById('profileForm');
  var avatarInput = document.getElementById('avatarInput');
  var loadingMessage = document.getElementById('loadingMessage');
  var successMessage = document.getElementById('successMessage');

  loadingMessage.style.display = 'block';

  var formData = new FormData(form);

  fetch(form.action, {
    method: form.method,
    body: formData
  })
  .then(response => response.json())
  .then(data => {
    loadingMessage.style.display = 'none';

    if (data.success) {
      successMessage.style.display = 'block';
      setTimeout(function() {
        successMessage.style.display = 'none';
        location.reload();
      }, 1000);  // Display success message for 1 seconds
    } else {
      alert('Error uploading file. Please try again.');
    }
  })
  .catch(error => {
    loadingMessage.style.display = 'none';
    alert('Error uploading file. Please try again.');
    console.error('Error:', error);
  });
}