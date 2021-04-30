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


$('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));






/*
    vanilla JavaScript for MaterializeCSS initialization
*/

// document.addEventListener('DOMContentLoaded', function () {
//     let sidenavs = document.querySelectorAll(".sidenav");
//     let sidenavsInstance = M.Sidenav.init(sidenavs, {edge: "right"});
// });