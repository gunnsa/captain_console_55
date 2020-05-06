$(document).ready(function () {
    $('#add_to_cart_btn').on('click', function(e){
        e.preventDefault();
        var cartItemId = $(this).attr('data-id');
        console.log(cartItemId)
        $.ajax({
            url: '/products/' + cartItemId + '/add_to_cart',
            type: 'POST',
            success: function (resp) {
                alert("SUCCESS!")
            },
            error: function (status, error) {
                alert("ERROR")

            }

        });
    })
})
