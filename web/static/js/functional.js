var msg_template = `
        <button class="paster-button-object">{text}<p class="date">---{date}</p></button>`,
        $messagesContainer = $('#mess_form');

eel.expose(push_data)
function push_data(values){
    var elementSplits = values.splice("---");
    var msg = msg_template
        .replace("{text}", elementSplits[0])
        .replace("{date}", elementSplits[1])
    $messagesContainer.prepend(msg).find(":first").slideUp(0).slideDown("fast");
}

eel.expose(share_data)
function share_data(values){
    for (index = 0; index < values.length; ++index){
        var element = values[index];
        var elementSplits = element.split("---");
        var msg = msg_template
            .replace("{text}", elementSplits[0])
            .replace("{date}", elementSplits[1])
        $messagesContainer.prepend(msg).find(":first").slideUp(0).slideDown("fast");
    }
}

window.onresize = function () {
    window.resizeTo(900, 500);
}
