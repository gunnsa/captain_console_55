$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $(this).attr('data-name');

        console.log('searchText: ', searchText)
        $.ajax( {
            url: '/products?drop_filter=' + searchText,
            type: 'GET',
            
            success: function (resp) {
              var newHtml = resp.data.map(d => {
                  return `<div class='well product'>
                      <a href='/products/${d.id}'>
                        <img class="product-img" src="${d.firstImage}"/>
                        <h4>${d.name}</h4> 
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
