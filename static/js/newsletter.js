$(document).ready(function () {
    $('#add_to_newsletter_btn').on('click', function(e){
        e.preventDefault();
        swal({
            text: "Please enter your email",
            content: "input",
        })
            .then((email) => {
                console.log(email)
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
                error: function (status, error) {
                swal({
                    text: "Woops! try again",
                    icon: "warning",
                    buttons: false,
                    });
                    }
                });
            });
    })
})