$(document).ready(function () {
    // for first card
    $("#secondslide").hide();
    $("#right").click(function () {
        $("#firstslide").toggle(1000);
        $("#secondslide").toggle(1000);
    })
    $("#left").click(function () {
        $("#firstslide").toggle(1000);
        $("#secondslide").toggle(1000);
    })

    // for third card
    $("#secondslide2").hide();
    $("#right2").click(function () {
        $("#firstslide2").toggle(1000);
        $("#secondslide2").toggle(1000);
    })
    $("#left2").click(function () {
        $("#firstslide2").toggle(1000);
        $("#secondslide2").toggle(1000);
    })




    // bbbbbbbbbbbbbbbbbbbbbbbb
    $("#particulars").hide();
    $("#aspect").hide();
    $("#question-answer").hide();
    $("#particulars-button").click(function(){
        $("#critique").hide();
        $("#aspect").hide();
        $("#question-answer").hide();
        $("#particulars").show();
    })
    $("#aspect-button").click(function(){
        $("#critique").hide();
        $("#particulars").hide();
        $("#question-answer").hide();
        $("#aspect").show();
    })
    $("#critique-button").click(function(){
        $("#particulars").hide();
        $("#aspect").hide();
        $("#question-answer").hide();
        $("#critique").show();
    })
    $("#question-answer-button").click(function(){
        $("#particulars").hide();
        $("#aspect").hide();
        $("#critique").hide();
        $("#question-answer").show();
    })


        // draggabe menu
        $( "#draggable" ).draggable();
  
});




$(".rectangle56").click(function(){
    $("#shoppingBagSvgrepoCom02").animate({
        left: '202px',
       top:'-557px',
       opacity: '0.0'
    }, "slow");
  });
  


    
    




window.onscroll = function () { myFunction() };

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myFunction() {
        if (window.pageYOffset > sticky) {
                header.classList.add("sticky");
        } else {
                header.classList.remove("sticky");
        }
}
$(document).ready(function () {
        $('[data-toggle="popover"]').popover();
});








// card1


