$(document).ready(function () {
    $('#contact-info').on('click', function(e){
        $.ajax({
            url: '/order/create',
            type: 'POST',
            success: function (resp) {
                alert("Order created")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
})

$(document).ready(function () {
    $('#processed-order').on('click', function(e){
        $.ajax({
            url: '/order/payment/create',
            type: 'POST',
            success: function (resp) {
                alert("Processed order created")
            },
            error: function (status, error) {
                alert("Whoops something went wrong :(")

            }
        });
    })
})





