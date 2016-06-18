$(document).ready(function(){

    $('.question').on('click', function(e){
        var active_answer = $('.active');

        /* when the page loads active answer will be none
         * therefore there are two cases to consider:
           <1> if active_answer is null- simply show the clicked answer
           and add the active class to it
           <2> if active_answer is not null, remove active from it, hide it, and add
           it to the clicked answer
         */
        var answer = $(this).siblings('.answer');
        if(answer.is(active_answer)){
            answer.toggle();
        } else {
            if (active_answer) {
                active_answer.removeClass('active');
                active_answer.hide();
                answer.addClass('active');
                answer.show();
            } else {
                answer.show();
                answer.addClass('.active');
            }
        }
    })
});
