/**
 * Created by georgi on 18/06/16.
 */
$(document).ready(function(){
    $("#search-term").keyup(function(){
        var text = $(this).val();
        /* create the ajax request */
        $.ajax({
            url: '/search_dictionary/',
            type: 'GET',
            data: {'search_term': text},
            success: function(data){
                $('#container-for-dict').html(data);
            }
        });
    });
});