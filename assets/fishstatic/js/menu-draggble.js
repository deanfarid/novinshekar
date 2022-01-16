$(document).ready(function () {
    // draggabe menu
    $("#draggable").draggable();


    // for first card
    $("#secondslide").hide();
    $("#right").click(function () {
        $("#firstslide").toggle(1000);
        $("#secondslide").toggle(1000);
    });
    $("#left").click(function () {
        $("#firstslide").toggle(1000);
        $("#secondslide").toggle(1000);
    });

    // for secound card
    $("#secondslide2").hide();
    $("#right2").click(function () {
        $("#firstslide2").toggle(1000);
        $("#secondslide2").toggle(1000);
    });
    $("#left2").click(function () {
        $("#firstslide2").toggle(1000);
        $("#secondslide2").toggle(1000);
    });
});