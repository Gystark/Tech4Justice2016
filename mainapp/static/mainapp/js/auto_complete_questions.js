/**
 * Created by georgi on 19/06/16.
 */
$(document).ready(function(){
    $("#search-term").keyup(function(){
        var search_term = $(this).val();
        var category_id = $('#category-id').val();
        $.ajax({
            url: '/search_questions/',
            data: {'search_term': search_term, 'category_id': category_id},
            type: "GET",
            success: function(data){
                $("#container-question").html(data);
            }
        });
    });
});