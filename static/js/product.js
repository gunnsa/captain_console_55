$(document).ready(function () {
    $('.search-btn').on('click', function (e) {
        e.preventDefault();
        console.log(this)
        var searchText = $(this).attr('data-name');
        $.ajax( {
            url: '/products?brand_filter=' + searchText,
            type: 'GET',

            success: function (resp) {
              var newHtml = resp.data.map(d => {
                  return `<div class='single-product'>
                          <a href='/products/${d.id}'>
                                <img class="product-img" src="${d.firstImage}"/>
                                <h4>${d.name}</h4> 
                                <p>${d.short_description}</p>
                                <p>${d.price}$</p>
                          </a>
                      </div>`
              });
              $('.products').html(newHtml.join(''));
              $('#search-btn').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});



$(document).ready(function () {
    $('.price-btn').on('click', function (e) {
        e.preventDefault();
        console.log(this)
        var searchText = $(this).attr('data-name');
        $.ajax( {
            url: '/products?price=' + searchText,
            type: 'GET',

            success: function (resp) {
              var newHtml = resp.data.map(d => {
                  return `<div class='single-product'>
                          <a href='/products/${d.id}'>
                                <img class="product-img" src="${d.firstImage}"/>
                                <h4>${d.name}</h4> 
                                <p>${d.short_description}</p>
                                <p>${d.price}$</p>
                          </a>
                      </div>`
              });
              $('.products').html(newHtml.join(''));
              $('#price-btn').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});

