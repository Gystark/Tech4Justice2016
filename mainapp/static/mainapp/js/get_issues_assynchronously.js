$(document).ready(function(){
    /* on click of the category link
     * send ajax request to the server
     * to display the issues related to the category*/
    $('.category-identifier').click(function(){
        /* take the category id */
        category_id = $(this).attr('value');
        /* make the ajax request */
        $.ajax({
            url: '/get_issues/',
            type: "GET",
            data: {'category_id': category_id},
            success: function(data){
                $('#issue-list').html(data);
            }
        })
    });
});