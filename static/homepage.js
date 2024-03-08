function display_data(newData){
  let result = ""; // Declare result variable
  three_data.forEach(function (data) {
      result += `
              <div class="${data.title} picks col-md-12 col-lg-4 col-sm-12 col-12">
              <div class=container-for-pick>
              <div class="pick-title">${data.title}</div>
              <div class="pick-image-container">
                <a href="/view/${data.id}">
                  <img class="pick-image" src="${data.image}" alt="image for picked restaurants">
                  </a>
              </div>
              <div class="reviews-username">${data.reviews[0].username}</div>
              <div class="reviews-rate">${data.reviews[0].rate}</div>
              <div class="reviews-review">${data.reviews[0].review}</div>

              </div>
              </div>
      `;
  });
  $(".kento-pick").append(result); // Set HTML content of .record
}
$(document).ready(function(){
  display_data(three_data)
})

