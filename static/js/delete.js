$(document).ready(function () {
    $('#remove_cart_item_btn').on('click', function(e){
        e.preventDefault();
        var cartId = $(this).attr('data-id');
        console.log(cartId)
        $.ajax({
            url: '/cart/' + cartId + '/remove_cart_item',
            type: 'POST',
            success: function (resp) {
                alert("Item removed from cart")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
})