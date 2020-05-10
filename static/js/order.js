$(document).ready(function () {
    $('#continue_to_payment').on('click', function(e){
        e.preventDefault();
        console.log(quantity)
        $.ajax({
            url: '/order/delivery',
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