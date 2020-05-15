$(document).ready(function () {
    $('#add-to-newsletter-btn').on('click', function(e){
        e.preventDefault();

        swal({
            text: "Please enter your email",
            content: "input",
        })
            .then((email) => {
                $.ajax({
                url: 'add_to_newsletter/' + email,
                type: 'POST',
                success: function (resp) {

                    swal({
                        text: "You have been signed!",
                        icon: "success",
                        buttons: false,
                        timer: 1450,});
                },
                error: function (xhr,status, error) {
                swal({
                    text: "Whoops! Please enter a valid email!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
                    }
                });
            });
    })
})