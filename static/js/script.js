/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $(".datepicker").datepicker({
        format: "yyyy",
        yearRange: 100,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});


$('.comment_submit').on('click', function(event){
    filmId = $(this).attr('data-film-id');
    comment = $('#' + $(this).attr('data-target_id')).val();
    requestData = {'id': filmId, 'comment': comment}
    console.log('add comment to Film id', filmId, comment);
    $.post( "/comment", requestData, function( data ) {
        commentsTargetId = '#film_comment_' + filmId;
        totalCommentsId = '#film_comment_total_' + filmId;
        newComment = '<div class="row"> <p>' + data.author + '</p> <p>' + data.text + '</p></div>';
        totalComments = parseInt($(totalCommentsId).text()) + 1;
        $(commentsTargetId).append(newComment);
        $('#new_comment_' + filmId).val('');
        $(totalCommentsId).text(totalComments);
    });
});






/*
    vanilla JavaScript for MaterializeCSS initialization
*/

// document.addEventListener('DOMContentLoaded', function () {
//     let sidenavs = document.querySelectorAll(".sidenav");
//     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
// });