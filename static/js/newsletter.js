$(document).ready(function () {
    $('#add-to-newsletter-btn').on('click', function(e){
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
                    console.log(resp)
                    console.log('hello', this.url)
                    swal({
                        text: "You have been signed!",
                        icon: "success",
                        buttons: false,
                        timer: 1450,});
                },
                error: function (xhr, status, error) {
                swal({
                    text: "Whoops! Try again!",
                    icon: "warning",
                    buttons: false,
                    timer: 1450,});
                    }
                });
            });
    })
})