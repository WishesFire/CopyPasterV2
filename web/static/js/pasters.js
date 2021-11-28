$(document).ready(function (){
    $('#mess_form').on("click", ".paster-button-object", function () {
        console.log("aloha");
        var text = $(this).text();
        var splitArrayText = text.split("---");
        eel.set_data(splitArrayText[0]);
    })

    $(".telegram-button").on("click", function (){
        eel.telegram_connection()
    })

    $(".archive-button").on("click", function (){
        eel.archive_show()
    })

    $(".reload-button").on("click", function (){
        $("#mess_form").empty();
        eel.reload_list()
    })
});
