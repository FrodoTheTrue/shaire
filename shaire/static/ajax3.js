function show()
        {
            a = []
            a = $("*").html()
            var count = 0;
            for (var i=0; i<a.length - 7;i++)
            {
                if (a[i] == 'm' &&
                    a[i + 1] == 's' &&
                    a[i + 2] == 'g' &&
                    a[i + 3] == '_' &&
                    a[i + 4] == 'h' &&
                    a[i + 5] == 'e' &&
                    a[i + 6] == 'r' &&
                    a[i + 7] == 'e'
                    )
                    count += 1;
            }
            console.log(count)
            $.ajax({
                type: "GET",
                url: "/im/check_new/",
                data: { count : count , user_to : "{{ user_to_username }}" },
                success: function(data){
                    if (data != "-1")
                        {
                        $("#messages").append(data);
                        $('#scroll-able').scrollTop( 100000000 );
                        }
                }
            });
        }

$(document).ready(function(){
    $('#scroll-able').scrollTop( 100000000 );
    show();
    setInterval('show()',1000);
});
