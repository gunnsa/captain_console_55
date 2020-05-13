
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
    $('.decrease_cart').on('click', function(e){
      e.preventDefault();
      var parent_value = this.parentNode.parentNode
      var child_value = parent_value.childNodes

      var value = parseInt(child_value[3].value, 10);
      value = isNaN(value) ? 0 : value;

      if (value == 1) {
          value = 1
      }
      else {
          value--;
      }
      child_value[3].value = value;
      child_value[3].innerHTML = value; //þannig við sjáum breytingu í HTML til að tengja við cart
    })

    $('.increase_cart').on('click', function(e){
        e.preventDefault();
        var parent_value = this.parentNode.parentNode
        var child_value = parent_value.childNodes

        var value = parseInt(child_value[3].value, 10);

        value = isNaN(value) ? 0 : value;
        value++;

        child_value[3].value = value;
        child_value[3].innerHTML = value; //þannig við sjáum breytingu í HTML til að tengja við cart
    })
});

$(document).ready(function () {
    $('.decrease_cart').on('click', function (e) {
        e.preventDefault();
        var cartid = $(this).attr('data-id');
        var parent_value = this.parentNode.parentNode
        var child_value = parent_value.childNodes

        var quantity = parseInt(child_value[3].value, 10);
        $.ajax({
            url: '/cart/' + cartid + '/update_cart/' + quantity,
            type: 'PATCH',
            success: function (resp) {

            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    });
    $('.increase_cart').on('click', function (e) {
        e.preventDefault();
        var cartid = $(this).attr('data-id');
        var parent_value = this.parentNode.parentNode
        var child_value = parent_value.childNodes

        var quantity = parseInt(child_value[3].value, 10);
        $.ajax({
            url: '/cart/' + cartid + '/update_cart/' + quantity,
            type: 'PATCH',
            success: function (resp) {
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")
            }
        });
    });
    $('.remove_cart_item_btn').on('click', function(e){
        e.preventDefault();
        console.log('remove item pushed')
        var cartId = $(this).attr('data-id');
        $.ajax({
            url: '/cart/' + cartId + '/remove_cart_item',
            type: 'DELETE',
            success: function (resp) {
                swal({
                    text: "Item removed from cart!",
                    icon: "success",
                    buttons: false,});
                window.location.replace("/cart/")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
})
