$(document).ready(function () {
    $('#add_to_cart_btn').on('click', function(e){
        e.preventDefault();
        var cartItemId = $(this).attr('data-id');
        var quantity = $('#quantity').val()

        $.ajax({
            url: '/products/' + cartItemId + '/add_to_cart/' + quantity,
            type: 'POST',
            success: function (resp) {
                swal("Here's a message!")
                alert("Item added to cart")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")
            }
        });
    })
})


