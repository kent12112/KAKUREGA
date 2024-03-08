$(document).ready(function () {
  $("#searchForm").submit(function (event) {
    event.preventDefault();

    // Get the search input value
    var searchInputValue = $('#searchInput').val().trim();

    // Construct the URL with the search query
    var redirectUrl = "";  // Initialize redirectUrl

    if (searchInputValue !== "") {
      redirectUrl = `/search/${encodeURIComponent(searchInputValue)}`;
      window.location.href = redirectUrl;
    } else {
      // Handle the case when the search input is empty
      redirectUrl = `/search/`;
      $("#searchInput").val('');
      $("#searchInput").focus();
    }

    // Redirect to the new page
  });
});
