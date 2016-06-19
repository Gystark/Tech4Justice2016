/**
 * Created by georgi on 19/06/16.
 */
$(document).ready(function(){
    $('#search-term').keyup(function(){
        var search_term = $(this).val();
        $.ajax({
            url: '/search_categories/',
            type: "GET",
            data: {'search_term': search_term},
            success: function (data) {
                console.log(data);
                $('#container-for-cats').html(data);
            }
        });
    });
});