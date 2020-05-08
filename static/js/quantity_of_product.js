$(document).ready(function () {
    $('.decrease_value').on('click', function(e){
      e.preventDefault();

      var DEC_cartId_this = $(this).attr('data-id');
      console.log('DEC_cartId_this: ', DEC_cartId_this);

      var DEC_cartid_qty = document.getElementById('quantity').getAttribute('data-id');
      console.log('DEC_cartid_qty: ', DEC_cartid_qty);

      var value = parseInt(document.getElementById('quantity').value,10);
      value = isNaN(value) ? 0 : value;

      if (value == 1) {
          value = 1
      }
      else {
          value--;
      }
      document.getElementById('quantity').value = value;
      document.getElementById('quantity').innerHTML = value; //þannig við sjáum breytingu í HTML til að tengja við cart
    })
})

$(document).ready(function () {
    $('.increase_value').on('click', function(e){
      e.preventDefault();

      var cartId_this = $(this).attr('data-id');
      console.log('cartId: ', cartId_this);

      var cartid_qty = document.getElementById('quantity').getAttribute('data-id');
      console.log('cartid_id: ', cartid_qty);

      var value = parseInt(document.getElementById('quantity').value,10);
      value = isNaN(value) ? 0 : value;
      value++;
      document.getElementById('quantity').value = value;
      document.getElementById('quantity').innerHTML = value; //þannig við sjáum breytingu í HTML til að tengja við cart
    })
})

