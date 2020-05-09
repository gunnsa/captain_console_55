$(document).ready(function () {
    $('.brand-btn').on('click', function (e) {
        e.preventDefault();
        console.log(this)
        var searchText = $(this).attr('data-name');
        console.log(this.url)
        $.ajax( {
            url: '/products?brand_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                console.log(this.url)
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
              $('#brand-btn').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});




var searchText = new URLSearchParams(window.location.search).get('search-text');
if (searchText != null){
    $.ajax( {
        url: '/products?search_filter=' + searchText,
        type: 'GET',
        success: function (resp) {
            console.log(this.url)
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

        },
        error: function (xhr, status, error) {
            console.error(error);
        }
    })
};




$(document).ready(function () {
    $('.price-btn').on('click', function (e) {
        e.preventDefault();
        console.log(this)
        var searchText = $(this).attr('data-name');
        console.log(this.url)

        $.ajax( {
            url: '/products?price=' + searchText,
            type: 'GET',

            success: function (resp) {
                console.log(this.url)
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



