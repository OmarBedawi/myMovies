/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
});


/*
    jQuery for comments in card reveal
*/


$('.comment_submit').on('click', function(event){
    filmId = $(this).attr('data-film-id');
    comment = $('#' + $(this).attr('data-target_id')).val();
    requestData = {'id': filmId, 'comment': comment};
    console.log('add comment to Film id', filmId, comment);
    $.post( "/comment", requestData, function( data ) {
        commentsTargetId = '#film_comment_' + filmId;
        totalCommentsId = '#film_comment_total_' + filmId;
        newComment = '<div class="row"> <p class="comment_author">' + data.author + '</p> <p>' + data.text + '</p>';
        newComment += '<a href="delete_film_comment/'+filmId+'/'+comment + '" class="btn-small red darken-1 col s4 remove_comment right" onclick="return confirm('+"'Remove this comment?')"+'"><h6 class="remove_comment_text ">Remove</h6></a> </div>';
        totalComments = parseInt($(totalCommentsId).text()) + 1;
        $(commentsTargetId).append(newComment);
        $('#new_comment_' + filmId).val('');
        $(totalCommentsId).text(totalComments);
    });
});
