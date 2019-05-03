
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}
function myInput(){
    $(document).ready(function(){
      $("#myInput").on("focusout", function() {
        var value = $(this).val().toLowerCase();

        $("#myTable tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
        total_itens();
      });
    });
}

//somar total das tabelas Itens
function total_itens() {
    var table = document.getElementById("myTable"),
        itens = 0,
        notas_list = [],
        sumItens=0.00,
        sumDesc=0.00,
        sumFretes=0.00,
        sumOutros=0.00,
        sumSeg=0.00;

    for (var i = 0; i < table.rows.length; i++) {

        if ($(table.rows[i]).is(":visible") === true) {
            sumItens = sumItens + parseFloat((table.rows[i].cells[3].innerHTML)
                .replace(".", "").replace(",", "."));
            sumDesc = sumDesc + parseFloat((table.rows[i].cells[4].innerHTML)
                .replace(".", "").replace(",", "."));
            sumFretes = sumFretes + parseFloat((table.rows[i].cells[5].innerHTML)
                .replace(".", "").replace(",", "."));
            sumOutros = sumOutros + parseFloat((table.rows[i].cells[6].innerHTML)
                .replace(".", "").replace(",", "."));
            sumSeg = sumSeg + parseFloat((table.rows[i].cells[7].innerHTML)
                .replace(".", "").replace(",", "."));

            if (notas_list.includes(table.rows[i].cells[1].textContent) === false){
                notas_list.push(table.rows[i].cells[1].textContent)
            }
            itens++;
        }
    }
    document.getElementById("sumItens").innerHTML = sumItens
        .toLocaleString("pt-BR", { style: "currency" , currency:"BRL"});

    document.getElementById("sumDesc").innerHTML = sumDesc
        .toLocaleString("pt-BR", { style: "currency" , currency:"BRL"});

    document.getElementById("sumFretes").innerHTML = sumFretes
        .toLocaleString("pt-BR", { style: "currency" , currency:"BRL"});

    document.getElementById("sumOutros").innerHTML = sumOutros
        .toLocaleString("pt-BR", { style: "currency" , currency:"BRL"});

    document.getElementById("sumSeg").innerHTML = sumSeg
        .toLocaleString("pt-BR", { style: "currency" , currency:"BRL"});

    document.getElementById("nItens").innerHTML = itens;
    document.getElementById("nNotas").innerHTML = notas_list.length;
}