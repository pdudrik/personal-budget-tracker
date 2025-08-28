let table = document.getElementById("table");

// Load data from selected row
table.onclick = (e) => {
    let targetRow = e.target.closest("tr");
    let recordId = targetRow.id;
    let form = document.getElementById("incomeForm");
    form.action = "/income/" + recordId + "/update";

    let ammountInput = document.getElementById("ammount");
    let sourceInput = document.getElementById("source");
    let tsInput = document.getElementById("ts");
    let noteInput = document.getElementById("note");

    ammountInput.value = targetRow.cells[1].textContent.split(" ")[0];
    sourceInput.value = targetRow.cells[0].textContent;
    noteInput.value = targetRow.cells[3].textContent;

    let tsValue = targetRow.cells[2].textContent;
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


function delete_income_record(recordId)
{
    const csrf = document.querySelector('#incomeForm input[name="csrf_token"]').value;
    let data = {"recordId": recordId};

    $.ajax({
        type: "POST",
        url: "/income/delete-record",
        data: JSON.stringify(data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        headers: { "X-CSRFToken": csrf },
        success: function(data) {
            window.location.reload();
        },
        error: function(errMsg) {
            alert(errMsg);
        }
    });
}
