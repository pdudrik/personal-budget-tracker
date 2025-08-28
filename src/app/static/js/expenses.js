let table = document.getElementById("table");

// Load data from selected row or press delete button
table.addEventListener("click", (e) => {
    const delButton = e.target.closest(".btn-del");
    if (delButton) {
        e.preventDefault();
        e.stopPropagation();
        delete_expenses_record(delButton.dataset.id);
        return;
    }

    const row = e.target.closest("tr");
    if (!row) return;

    let form = document.getElementById("expensesForm");
    form.action = "/expenses/" + row.id + "/update";

    let ammountInput = document.getElementById("ammount");
    let tsInput = document.getElementById("ts");
    let categoryInput = document.getElementById("category");
    let subcategoryInput = document.getElementById("subcategory");
    let noteInput = document.getElementById("note");

    ammountInput.value = row.cells[0].textContent.split(" ")[0];
    categoryInput.value = row.cells[2].textContent;
    subcategoryInput.value = row.cells[3].textContent;
    noteInput.value = row.cells[4].textContent;

    let tsValue = row.cells[1].textContent;
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
})


function cancel_selection()
{
    alert("Cancel");
}


function delete_expenses_record(recordId)
{
    const csrf = document.querySelector('#expensesForm input[name="csrf_token"]').value;
    let data = {"recordId": recordId};

    $.ajax({
        type: "POST",
        url: "/expenses/delete-record",
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
