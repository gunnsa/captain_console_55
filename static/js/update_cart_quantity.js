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




