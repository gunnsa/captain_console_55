$(document).ready(function () {
    $('#decrease').on('click', function(e){
      e.preventDefault();
      var value = parseInt(document.getElementById('quantity').value,10);
      value = isNaN(value) ? 0 : value;
      value < 1 ? value = 1 : '1';
      value--;
      document.getElementById('quantity').value = value;
      document.getElementById('quantity').innerHTML = value; //þannig við sjáum breytingu í HTML til að tengja við cart
    })
})

$(document).ready(function () {
    $('#increase').on('click', function(e){
      e.preventDefault();
      var value = parseInt(document.getElementById('quantity').value,10);
      value = isNaN(value) ? 0 : value;
      value++;
      document.getElementById('quantity').value = value;
      document.getElementById('quantity').innerHTML = value; //þannig við sjáum breytingu í HTML til að tengja við cart
    })
})
