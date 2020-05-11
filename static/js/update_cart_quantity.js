
//fá þegar quantity er hækkað, matcha við cart Id og skrifa aftur niður í db nýtt quantity, verðið þarf
//líka að uppfærast
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
    $('.decrease_value').on('click', function (e) {
        e.preventDefault();
        var cartid = $(this).attr('data-id');
        console.log('cartId', cartid)
        var parent_value = this.parentNode.parentNode
        child_value = parent_value.childNodes

        var quantity = parseInt(child_value[3].value, 10);
        console.log('val', quantity)
        console.log('next up ajax')
        $.ajax({
            url: '/cart/' + cartid + '/update_cart/' + quantity,
            type: 'POST',
            success: function (resp) {

            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
    $('.increase_value').on('click', function (e) {
        e.preventDefault();
        var cartid = $(this).attr('data-id');
        console.log('cartId', cartid)
        var parent_value = this.parentNode.parentNode
        child_value = parent_value.childNodes

        var quantity = parseInt(child_value[3].value, 10);
        console.log('val', quantity)
        console.log('next up ajax')
        $.ajax({
            url: '/cart/' + cartid + '/update_cart/' + quantity,
            type: 'POST',
            success: function (resp) {

            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    });
});









