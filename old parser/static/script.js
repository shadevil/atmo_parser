var date = new Date();

document.getElementById("datetime").innerHTML ="Обновлено в " +  Date();
function searching() {
  var input = document.getElementById("search");
        var filter = input.value.toUpperCase();
        var table = document.getElementById("maintable");
        var tr = table.getElementsByTagName("tr");
        var td, tdArr, i, j;

        for (i = 0; i < tr.length; i++) {
            tdArr = tr[i].getElementsByTagName("td");
            for (j = 0; j < tdArr.length; j++) {
                td = tdArr[j];
                if (td) {
                    if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
                        tr[i].style.display = "";
                        break;
                    } else {
                        tr[i].style.display = "none";
                    }
                }
            }
        }
    // // Declare variables
    // var input, filter, table, tr, td1, td2, td3, i, det;
    // input = document.getElementById("search");
    // filter = input.value.toUpperCase();
    // table = document.getElementById("maintable");
    // tr = table.getElementsByTagName("tr");
    // det = document.getElementsByTagName("details");
    // // Loop through all table rows, and hide those who don't match the search query
    // for (i = 0; i < tr.length; i++) {
    //   td1 = tr[i].getElementsByTagName("td")[1];
    //   td2 = tr[i].getElementsByTagName("td")[6];
    //   td3 = tr[i].getElementsByTagName("td")[7];
    //   if(td1)
    //   {
    //     //txtValue = td.textContent || td.innerText;
    //     if (td1.innerHTML.toUpperCase().indexOf(filter) > -1 || td2.innerHTML.toUpperCase().indexOf(filter) > -1 || td2.innerHTML.toUpperCase().indexOf(filter) > -1) {
        
    //       tr[i].style.display = "";
          
    //     } else {

    //     tr[i].style.display = "none";
        
    //     }
    //   }
    // }
  }
//var input = document.body.children[0];

// input.oninput = function() {
//     ("#firstInRow").find("tr:last-child").remove();
// document.getElementById("myTable").deleteRow(0);
// document.getElementById('result').innerHTML = input;
//
 //{% comment %} oninput: <span id="result"> {% endcomment %}}
//  for(var i=0; i<det.length;i++)
//         {
//           det[i].open = true;
//         }
