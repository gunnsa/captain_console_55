var searchText = new URLSearchParams(window.location.search).get('search-text');
if (searchText != null){
    $.ajax( {
        url: '/products?search_filter=' + searchText,
        type: 'GET',

        success: function (resp) {
          var newHtml = resp.data.map(d => {
              return `<div class='single-product'>
                      <a href='/products/${d.id}'>
                            <img class="product-img" src="${d.firstImage}"/>
                            <h4>${d.name}</h4> 
                      </a>
                            <p>${d.short_description}</p>
                            <p>${d.price}$</p>
                      
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
    $('.min-price-btn').on('click', function (e) {
        e.preventDefault();

        var sort_by = $(this).attr('data-name');
        var pathname = window.location.pathname;

        const childDivs = document.querySelectorAll('.single-product')
        console.log(childDivs)


        //var tilraun = document.getElementsByClassName('single-product')
        //console.log(tilraun)

        for (var i = 0; i < childDivs.length; i++) {
            console.log(childDivs[i])
            //if (childDivs[i].tagName == 'a' || childDivs[i].tagName == 'p') {
            //  console.log(childDivs[i])

                //console.log(childDivs[i].getAttribute('data-name'));
            //}
            if (childDivs[i].tagName == 'a') {
                console.log(childDivs[i])
            }
        }

        //var hello = tilraun[1].childNodes

        //console.log(hello)

        $.ajax({
            url: pathname + '?min_price=' + sort_by,
            type: 'GET',

            success: function (resp) {
                console.log(resp)
              var newHtml = resp.data.map(d => {
                  return `<div class='single-product'>
                          <a href='/products/${d.id}'>
                                <img class="product-img" src="${d.firstImage}"/>
                                <h4>${d.name}</h4> 
                          </a>
                                <p>${d.short_description}</p>
                                <p>${d.price}$</p>
                      </div>`
              });
              $('.products').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});


$(document).ready(function () {
    $('.max-price-btn').on('click', function (e) {
        e.preventDefault();
        var sort_by = $(this).attr('data-name');
        var pathname = window.location.pathname;

        $.ajax( {
            url: pathname + '?max_price=' + sort_by,
            type: 'GET',

            success: function (resp) {
                console.log(resp)
              var newHtml = resp.data.map(d => {

                  return `<div class='single-product'>
                          <a href='/products/${d.id}'>
                                <img class="product-img" src="${d.firstImage}"/>
                                <h4>${d.name}</h4> 
                          </a>
                                <p>${d.short_description}</p>
                                <p>${d.price}$</p>
                      </div>`
              });
              $('.products').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});



$(document).ready(function () {
    $('.name-btn').on('click', function (e) {
        e.preventDefault();
        var sort_by = $(this).attr('data-name');
        var pathname = window.location.pathname;

        $.ajax( {
            url: pathname + '?name=' + sort_by,
            type: 'GET',

            success: function (resp) {
              var newHtml = resp.data.map(d => {
                  return `<div class='single-product'>
                          <a href='/products/${d.id}'>
                                <img class="product-img" src="${d.firstImage}"/>
                                <h4>${d.name}</h4> 
                          </a>
                                <p>${d.short_description}</p>
                                <p>${d.price}$</p>
                      </div>`
              });
              $('.products').html(newHtml.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    });
});
