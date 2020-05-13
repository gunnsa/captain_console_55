$(document).ready(function () {
    $('#add_to_wishlist_btn').on('click', function(e){
        e.preventDefault();
        var wishlistItemId = $(this).attr('data-id');

        $.ajax({
            url: '/products/' + wishlistItemId + '/add_to_wishlist',
            type: 'POST',
            success: function (resp) {
                //swal("Here's a message!")
                alert("Item added to wishlist")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
    $('.remove_wishlist_item_btn').on('click', function(e){
        console.log('remove item pushed')
        var wishlistId = $(this).attr('data-id');
        console.log('wishlistId: ', wishlistId)
        $.ajax({
            url: '/wishlist/' + wishlistId + '/remove_wishlist_item',
            type: 'DELETE',
            success: function (resp) {
                window.location.replace("/wishlist/")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
    $('.add_to_cart_btn-wishlist').on('click', function(e){
        e.preventDefault();
        var wishlistItemId = $(this).attr('data-id');
        console.log('wishlistItemId: ', wishlistItemId)

        $.ajax({
            url: '/wishlist/' + wishlistItemId + '/add_to_cart/',
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


