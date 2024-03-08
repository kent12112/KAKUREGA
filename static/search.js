$(document).ready(function () {
    if (search_term) {
        if (data.length > 0) {
            display_data(search_term, data)
        } else {
            no_results(search_term)
        }
    }

    function display_data(input, newData) {
        let numOfResults = newData.length
        let result = `<div class="search_results col-lg-12 col-md-12"> ${numOfResults} results for "${input}"</div>`;
        newData.forEach(function (data) {
            // Highlight the search term in various fields
            const highlightedTitle = highlightSubstring(data.title, input);
            const highlightedReview = highlightSubstring(data.reviews[0].review, input);
            const highlightedTypes = highlightArray(data.types, input);

            result += `
                <div class="record-card col-md-12 col-lg-12">
                    <a href="/view/${data.id}">
                        <div class="container-for-record row">
                            <div class="record-image-container col-md-3.5 col-lg-3.5">
                                <img class="record-image" src="${data.image}" alt="image for searched restaurants">
                            </div>
                            <div class="record-details col-md-8 col-lg-8">
                                <div class="record-title">${highlightedTitle}</div>
                                <!-- Add other details here -->
                                <div class="record-types">${highlightedTypes.join('')}</div>
                                <div class="record-price">$${data.price}</div>
                                <div class="record-area">${data.area}</div>
                                <div class="record-reviews">💬 ${highlightedReview}</div>
                            </div>
                        </div>
                    </a>
                </div>
            `;
        });
        $(".record").html(result); // Set HTML content of .record
    }

    function no_results(input) {
        $(".record").html(
            `<div class="search_results">0 results for "${input}"</div>`
        )
    }

    function highlightSubstring(text, searchTerm) {
        // Highlight the search term in the text
        return text.replace(new RegExp(searchTerm, 'gi'), match => `<span class="highlight">${match}</span>`);
    }
    function highlightArray(array, searchTerm) {
        // Highlight the search term in each element of the array
        return array.map(element => `<a href="/search/${element}"><div class="eachtype">${highlightSubstring(element, searchTerm)}</div></a>`);
    }
});


    