
function display_data(oneData){
  const types = oneData.types.map(element => `<a href="/search/${element}"><div class="eachtype">${element}</div></a>`).join('');
  let result = "";
  result += `
    <div class="main row">
    <div class="left-side col-lg-7 col-md-7"> 
      <div class="title-price">
        <div class="title">${oneData.title}</div>
        <span class="price">${oneData.price}</span>
      </div>
      <img class="image" src="${oneData.image}" alt="the image of the selected restaurant">
      <div><a class="visit" href="${oneData.webpage}">Visit webpage</a></div>
      <div class="about">About The Restaurant</div>
      <div class="summary">${oneData.summary}</div>
    </div>
    <div class="right-side col-lg-5 col-md-5">
      <div class="popular-title">Popular dishes</div>
      <div class="popular">
      <ul>
        ${oneData.popular.map(dish => `<li class="dishes">${dish}</li>`).join('')}
      </ul>
    </div>
    <div class="types-title">Types</div>
    <div class="types">
        ${types}
      </div>
    <div class="reviews-title">Recommended Review</div>
    <div class="review-content">
    <div class="reviews-username">${oneData.reviews[0].username}</div>
    <div class="reviews-rate">${oneData.reviews[0].rate}</div>
    <div class="reviews-review">${oneData.reviews[0].review}</div>
    </div>
    </div>
    </div>
  `;
  $(".view").html(result);
}
console.log(oneData)
$(document).ready(function(){
  display_data(oneData)
});
