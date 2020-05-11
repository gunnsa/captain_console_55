$(document).ready(function () {
    $('.decrease_value').on('click', function(e){
      e.preventDefault();
      var parent_value = this.parentNode.parentNode
      child_value = parent_value.childNodes

      var value = parseInt(child_value[3].value, 10);
      console.log(value)
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
    $('.increase_value').on('click', function(e){
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

