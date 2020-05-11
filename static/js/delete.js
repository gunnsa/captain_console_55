$(document).ready(function () {
    $('.remove_cart_item_btn').on('click', function(e){
        e.preventDefault();
        var cartId = $(this).attr('data-id');
        console.log("js-cartid",cartId)
        $.ajax({
            url: '/cart/' + cartId + '/remove_cart_item',
            type: 'DELETE',
            success: function (resp) {
                console.log("success")
                alert("Item removed from cart")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        })
    })
});