
//var input = document.body.children[0];

// input.oninput = function() {
//     ("#firstInRow").find("tr:last-child").remove();
// document.getElementById("myTable").deleteRow(0);
// document.getElementById('result').innerHTML = input;
//
 //{% comment %} oninput: <span id="result"> {% endcomment %}}

<script>
function searching()
{
    var input, filter, table, tr, td1, td2, i, txtValue;
    input = document.getElementById("search");
    filter = input.value.toLowerCase();
    table = document.getElementById("maintable");
    tr = table.getElementsByTagName("tr");
    for(var i = 0; i < tr.length; ++i)
    {
        td1 = tr[i].getElementsByTagName("td")[1];
        //td2 = tr[i].getElementsByTagName("td")[6];
        txtValue1 = td1.textContent || td1.innerText;
        //txtValue2 = td2.textContent || td2.innerText;
        //|| txtValue2.toLowerCase().indexOf(search) > -1
        if (txtValue1.toLowerCase().indexOf(search) > -1 )
        {
            tr[i].style.display = "";
        }
        else
        {
            tr[i].style.display = "none";
        }
    }
}
</script>