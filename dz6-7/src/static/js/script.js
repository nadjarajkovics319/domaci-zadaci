
function updateRasporedTable() {
    let index = 0;
    var value = $(this).val() ? $(this).val().toLowerCase() : $(this).text().toLowerCase();

    $("#raspored tr").each(function(ind, el){
        $(el).removeClass('table-row');
        $(el).removeClass('odd-row');
        $(el).removeClass('even-row');
    });

    $("#raspored tr").each(function (ind, el) {
        if($(el).text().toLowerCase().indexOf(value) > -1){
            $(el).addClass('table-row');
            if(index++ % 2){
                $(el).addClass('odd-row');
            }else{
                $(el).addClass('even-row');
            }
        }
    });
}

$(document).ready(function () {
    $("#inputPolje").on("keyup", updateRasporedTable);
    $(".profesor").on("click",updateRasporedTable);
    $(".ucionica").on("click", updateRasporedTable);
    $('#inputPolje').trigger('keyup');
});