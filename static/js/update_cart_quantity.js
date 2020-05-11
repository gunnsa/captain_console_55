$(document).ready(function () {
    $('.decrease_cart').on('click', function(e){
      e.preventDefault();
      var parent_value = this.parentNode.parentNode
      child_value = parent_value.childNodes

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
})
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
    $('.increase_cart').on('click', function(e){
      e.preventDefault();
      var parent_value = this.parentNode.parentNode
      child_value = parent_value.childNodes

      var value = parseInt(child_value[3].value, 10);
      console.log(value)

      value = isNaN(value) ? 0 : value;
      value++;

      child_value[3].value = value;
      child_value[3].innerHTML = value; //þannig við sjáum breytingu í HTML til að tengja við cart
    })
})






$(document).ready(function () {
    $('.decrease_cart').on('click', function (e) {
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
                alert("Quantity updated")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });

        if (window.location.href == 'http://127.0.0.1:8000/cart/'){
        }
    })
});

//fá þegar quantity er hækkað, matcha við cart Id og skrifa aftur niður í db nýtt quantity, verðið þarf
//líka að uppfærast




