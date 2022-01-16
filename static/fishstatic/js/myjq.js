$(document).ready(function () {
    // for slide menu
    $(".nav").hide();
    $(".rectangle6").hover(function () {
        $(".x75ce7c6f").toggle(400 , function(){
           $(".nav").toggle(0); 
        }); 
    }, function () {
        $(".nav").toggle(0 , function(){
            $(".x75ce7c6f").toggle(1000);
        });
    });

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

    // for middle gigcard
    $("#middlefirstcard2").hide();
    $("#right3").click(function () {
        $("#middlefirstcard").toggle(1000);
        $("#middlefirstcard2").toggle(1000);
    })
    $("#left3").click(function () {
        $("#middlefirstcard").toggle(1000);
        $("#middlefirstcard2").toggle(1000);
    })


    // for buttons of moratab sazi
    $(".rectangle29").click(function () {
        $(".rectangle29").toggleclass(".activate");
        $(".x72b63841").toggleclass(".activate-text");
    })

    $(".rectangle30").click(function () {
        $(".rectangle30").addclass(".activate");
        $(".x74208968").addclass(".activate-text");
    })

    $(".rectangle31").click(function () {
        $(".rectangle31").toggleclass(".activate");
        $(".x72de76d9").toggleclass(".activate-text");
    })

    $(".rectangle28").click(function () {
        $(".rectangle28").toggleclass(".activate");
        $(".xdc513416").toggleclass(".activate-text");
    })

    $(".rectangle27").click(function () {
        $(".rectangle27").toggleclass(".activate");
        $(".xfdf035c1").toggleclass(".activate-text");
    })

    $(".rectangle26").click(function () {
        $(".rectangle26").toggleclass(".activate");
        $(".xdca5b896").toggleclass(".activate-text");
    })

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
