//------CSRF TOKEN------//
$(document).ready(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});



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

        $.ajax({
            url: pathname + '?min_price=' + sort_by,
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
                swal({
                    text: "Whoops! Try again!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
            }
        })
    });

    $('.max-price-btn').on('click', function (e) {
        e.preventDefault();
        var sort_by = $(this).attr('data-name');
        var pathname = window.location.pathname;

        $.ajax( {
            url: pathname + '?max_price=' + sort_by,
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
                swal({
                    text: "Whoops! Try again!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
            }
        })
    });

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
                swal({
                    text: "Whoops! Try again!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
            }
        })
    });





});




