let table = document.getElementById("table");

table.onclick = (e) => {
    let targetRow = e.target.parentElement;
    let recordId = targetRow.id;
    console.log(recordId);
    let form = document.getElementById("expensesForm");
    form.action = "/expenses/" + recordId + "/update";


    let ammountInput = document.getElementById("ammount");
    let tsInput = document.getElementById("ts");
    let categoryInput = document.getElementById("category");
    let subcategoryInput = document.getElementById("subcategory");
    let noteInput = document.getElementById("note");

    ammountInput.value = targetRow.cells[0].textContent.split(" ")[0];
    categoryInput.value = targetRow.cells[2].textContent;
    subcategoryInput.value = targetRow.cells[3].textContent;
    noteInput.value = targetRow.cells[4].textContent;

    let tsValue = targetRow.cells[1].textContent;
    let raw = (tsValue || "").trim();

    // robust parse: "dd.mm.yyyy" (ignores any trailing text/time)
    const m = raw.match(/^(\d{1,2})\.(\d{1,2})\.(\d{4})/);
    if (m) {
        const d  = m[1].padStart(2, "0");
        const mo = m[2].padStart(2, "0");
        const y  = m[3];
        tsInput.value = `${y}-${mo}-${d}`;
    } else {
        tsInput.value = "";
    }
}


function cancel_selection()
{
    alert("Cancel");
}


function delete_expenses_record(recordId)
{
    let data = {"recordId": recordId};

    $.ajax({
        type: "POST",
        url: "/expenses/delete-record",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            window.location.reload();
        },
        error: function(errMsg) {
            alert(errMsg);
        }
    });
}
