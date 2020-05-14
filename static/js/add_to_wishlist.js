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



$(document).ready(function () {
    $('#add-to-wishlist-btn').on('click', function(e){
        e.preventDefault();
        
        var wishlistItemId = $(this).attr('data-id');

        $.ajax({
            url: '/products/' + wishlistItemId + '/add_to_wishlist',
            type: 'POST',
            success: function (resp) {
                swal({
                    text: "Item added to wishlist!!",
                    icon: "success",
                    buttons: false,
                    timer: 1450,});
            },
            error: function (status, error) {
                swal({
                    text: "Whoops! Try again!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
            }
        });
    })
    $('.remove-wishlist-item-btn').on('click', function(e){
        e.preventDefault();

        var wishlistId = $(this).attr('data-id');

        $.ajax({
            url: '/wishlist/' + wishlistId + '/remove_wishlist_item',
            type: 'DELETE',
            success: function (resp) {
                swal({
                    text: "Item removed from wishlist!",
                    icon: "success",
                    buttons: false,
                    timer: 1450,});
                window.location.replace("/wishlist/")
            },
            error: function (status, error) {
                swal({
                    text: "Whoops! Try again!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
            }
        });
    })
    $('.add-to-cart-btn-wishlist').on('click', function(e){
        e.preventDefault();

        var wishlistItemId = $(this).attr('data-id');

        $.ajax({
            url: '/wishlist/' + wishlistItemId + '/add_to_cart/',
            type: 'POST',
            success: function (resp) {
                swal({
                    text: "Item added to cart!",
                    icon: "success",
                    buttons: false,
                    timer: 1450,});
                window.location.replace("/wishlist/")
            },
            error: function (status, error) {
                swal({
                    text: "Whoops! Try again!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
            }
        });
    })
})


