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


