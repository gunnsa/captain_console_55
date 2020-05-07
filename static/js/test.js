$(document).ready(function () {
    $('#add_to_cart_btn').on('click', function(e){
        e.preventDefault();
        var cartItemId = $(this).attr('data-id');
        var quantity = $('#quantity').val()
        console.log(quantity)
        $.ajax({
            url: '/products/' + cartItemId + '/add_to_cart/' + quantity,
            type: 'POST',
            success: function (resp) {
                alert("Item added to cart")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
})


function add_to_cart(productid, productname){
    //check if user logged in, if not, error message please log in
    //if logged in then axaj request to server
    //server updates cart db table
    //hluti af fallinu er jquery

    console.log(productid, productname)
}