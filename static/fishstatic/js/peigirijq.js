var $scroller = $('#scrollerd');
var dic = 1;

function sc() {
    // get the partial id of the div to scroll to
    var divIdx = $('#input-none').val();
    divIdx = parseInt(divIdx);
    if (dic == 1)
        divIdx = parseInt(divIdx) + 1;
    else
        divIdx = parseInt(divIdx) - 1;
    var count = $("#scrollerd #containerrd div").length;
    //console.log(count)
    cWidth = $('#containerrd').width()
    sWidth = $('#scrollerd').width()

    if (divIdx != 0 && divIdx <= count) {

        var scrollTo = $($('#scrollerd #containerrd div')[divIdx - 1])
            // change its bg
            .css('background', 'white')
            .position().left;
        if ((cWidth - scrollTo) > sWidth) {
            console.log('ok', cWidth, sWidth, scrollTo)

            $scroller
                .animate({
                    'scrollLeft': scrollTo
                }, 700);

            $('#input-none').val(divIdx);
        }
    }
} //func

// assign click handler
$('#leftddd').on('click', function () {
    dic = 0;
    sc();
});
$('#rightddd').on('click', function () {
    dic = 1;
    sc();
});




// afzayesh va kahesh tedad mahsol
var dik=1;
function src() {
    // get the partial id of the div to scroll to
    var divIdxx = $('#input').val();
    divIdxx = parseInt(divIdxx);
    if (dik == 1)
        divIdxx = parseInt(divIdxx) + 1;
        
    else
        divIdxx = parseInt(divIdxx) - 1;
        $('#input').val(divIdxx);
}
// assign click handler
$('#minus').on('click', function () {
    dik = 0;
    src();
    if($('#input').val()==1){
        $('#minus').hide();
    }else{
        $('#minus').show();
    }
});
$('#plus').on('click', function () {
    dik = 1;
    src();
    if($('#input').val()==1){
        $('#minus').hide();
    }else{
        $('#minus').show();
    }
});

$(document).ready(function(){
    $('#delete').click(function(){
        $('#name').hide();
    })
});
// /////////////////afzayesh va kahesh tedad mahsol//////////////////////

