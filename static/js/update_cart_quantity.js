//fá þegar quantity er hækkað, matcha við cart Id og skrifa aftur niður í db nýtt quantity, verðið þarf
//líka að uppfærast

$(document).ready(function () {
    $('#decrease.decrease_value').on('click', function (e) {
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
    })
});




