$(document).ready(function(){
    $('#scroll-able').scrollTop( 100000000 );
    $('#submt_{{ user_to_username }}').click(function(){
        var message = $("#text").val();
        $.ajax({
            type: "GET",
            url: "/im/send_message/",
            data: { text_message : message , user_name : "{{ user_to_username }}" }
        })
        .done(function(data) {
            $('#messages').append(data);
            $('#scroll-able').scrollTop( 100000000 );
            $("#text").val("");
            $('#text').focus();
        });
    });
})
