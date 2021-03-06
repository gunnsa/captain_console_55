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
    $('#add-to-cart-btn').on('click', function(e){
        e.preventDefault();
        var cartItemId = $(this).attr('data-id');
        var quantity = $('#quantity').val()

        $.ajax({
            url: '/products/' + cartItemId + '/add_to_cart/' + quantity,
            type: 'POST',
            success: function (resp) {
                swal({
                    text: "Item added to cart!",
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
});
