$(document).ready(function () {
  $('#title').val(item.title);
  $('#image').val(item.image);
  $('#webpage').val(item.webpage);
  $('#price').val(item.price);
  $('#summary').val(item.summary);
  $('#popular').val(item.popular.join(', '));
  $('#types').val(item.types.join(', '));
  $('#username').val(item.reviews[0].username);
  $('#rate').val(item.reviews[0].rate);
  $('#review').val(item.reviews[0].review);
  $('#area').val(item.area);

  $('#id').focus(); // Set focus on the first input field

  window.addItem = function () {
    // Prevent default form submission
    event.preventDefault();

    // Clear previous error messages
    clearErrorMessages();

    // Check if required fields are filled
    const requiredFields = ['title', 'area', 'image', 'summary', 'popular', 'types', 'webpage', 'price', 'username', 'rate', 'review'];
    for (const field of requiredFields) {
      const fieldValue = $(`#${field}`).val().trim();
      if (fieldValue === '') {
        // Display an error message next to the respective input field
        $(`#${field}Error`).text(`${field.charAt(0).toUpperCase() + field.slice(1)} is required.`);
      }
    }
    const priceInput = $('#price').val().trim();
    const validPrice = ['$', '$$', '$$$'];
    if (priceInput && !validPrice.includes(priceInput)) {
      $('#priceError').text('Price must be $, $$, or $$$.');
    }
    const rateInput = $('#rate').val().trim();
    const validRate = ['⭐️', '⭐️⭐️', '⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️', '⭐️⭐️⭐️⭐️⭐️'];
    if (rateInput && !validRate.includes(rateInput)) {
      $('#rateError').text('Price must be ⭐️, ⭐️⭐️, ⭐️⭐️⭐️, ⭐️⭐️⭐️⭐️, or ⭐️⭐️⭐️⭐️⭐️');
    }


    // Check if any errors were found
    if ($('.error').text() !== '') {
      return; // Stop form submission if any required field is empty
    }

    // Get form data
    const formData = $('#addItemForm').serializeArray();
    // Convert form data to an object
    const itemData = {};
    formData.forEach(field => itemData[field.name] = field.value);

    // Make an AJAX request to add the new item
    $.ajax({
      type: 'POST',
      url: `/edit/${item.id}`,
      data: $('#addItemForm').serialize(),
      success: function (response) {
        window.location.href = `/view/${response.item_id}`;
        // Clear the form
        $('#addItemForm')[0].reset();
        // Set focus on the first input field
        $('#title').focus();

      },
      error: function (error) {
        // Handle errors, e.g., show an error message
        alert(error.responseJSON.error);
      }
    });
  };

  // Bind the addItem function to the submit event of the form
  $('#addItemForm').on('submit', window.addItem);

  // Function to clear error messages
  function clearErrorMessages() {
    $('.error').text('');
  }
});

function discardChanges() {
  // Ask for confirmation before discarding changes
  const confirmDiscard = confirm("Are you sure you want to discard changes?");

  if (confirmDiscard) {
      // If confirmed, redirect to the view page without saving changes
     window.location.href = `/view/${item.id}`;
  }
}