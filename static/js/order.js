$(document).ready(function () {
    $('#contact-info').on('click', function(e){
        console.log(quantity)
        $.ajax({
            url: '/order/create',
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


