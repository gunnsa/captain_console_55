//fá þegar quantity er hækkað, matcha við cart Id og skrifa aftur niður í db nýtt quantity, verðið þarf
//líka að uppfærast

$(document).ready(function () {
    $('#decrease.decrease_value').on('click', function(e){
        e.preventDefault();
        var cartId = $(this).attr('data-id');
        console.log('cartId',cartId)
        var parent_value = this.parentNode.parentNode
        child_value = parent_value.childNodes

        var value = parseInt(child_value[3].value, 10);
        console.log('val',value)
    })
    $('#increase.increase_value').on('click', function(e){
        e.preventDefault();
        var cartId = $(this).attr('data-id');
        console.log('cartId',cartId)
        var parent_value = this.parentNode.parentNode
        child_value = parent_value.childNodes

        var value = parseInt(child_value[3].value, 10);
        console.log('val',value)
    })
})


