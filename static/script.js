function searching() {
    // Declare variables
    var input, filter, table, tr, td1, td2, i;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("maintable");
    tr = table.getElementsByTagName("tr");
    
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      td1 = tr[i].getElementsByTagName("td")[1];
      td2 = tr[i].getElementsByTagName("td")[6];
      if(td1)
      {
        //txtValue = td.textContent || td.innerText;
        if (td1.innerHTML.toUpperCase().indexOf(filter) > -1 || td2.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        } else {
        tr[i].style.display = "none";
        }
      }
    }
  }
//var input = document.body.children[0];

// input.oninput = function() {
//     ("#firstInRow").find("tr:last-child").remove();
// document.getElementById("myTable").deleteRow(0);
// document.getElementById('result').innerHTML = input;
//
 //{% comment %} oninput: <span id="result"> {% endcomment %}}
