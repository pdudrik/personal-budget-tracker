let table = document.getElementById("table");

// Load data from selected row or press delete button
table.addEventListener("click", (e) => {
    const delButton = e.target.closest(".btn-del");
    if (delButton) {
        e.preventDefault();
        e.stopPropagation();
        delete_goals_record(delButton.dataset.id);
        return;
    }

    const row = e.target.closest("tr");
    if (!row) return;

    let form = document.getElementById("goalsForm");
    form.action = "/goals/" + row.id + "/update";

    let nameInput = document.getElementById("name");
    let deadlineInput = document.getElementById("deadline");
    let targetAmmountInput = document.getElementById("targetAmmount");
    let currentAmmountInput = document.getElementById("currentAmmount");
    let noteInput = document.getElementById("note");

    nameInput.value = row.cells[0].textContent;
    targetAmmountInput.value = row.cells[2].textContent.split(" ")[0];
    currentAmmountInput.value = row.cells[3].textContent.split(" ")[0];
    noteInput.value = row.cells[4].textContent;

    let deadlineValue = row.cells[1].textContent;
    let raw = (deadlineValue || "").trim();

    // robust parse: "dd.mm.yyyy" (ignores any trailing text/time)
    const m = raw.match(/^(\d{1,2})\.(\d{1,2})\.(\d{4})/);
    if (m) {
        const d  = m[1].padStart(2, "0");
        const mo = m[2].padStart(2, "0");
        const y  = m[3];
        deadlineInput.value = `${y}-${mo}-${d}`;
    } else {
        deadlineInput.value = "";
    }
})


function cancel_selection()
{
    alert("Cancel");
}


function delete_goals_record(recordId)
{
    const csrf = document.querySelector('#goalsForm input[name="csrf_token"]').value;
    let data = {"recordId": recordId};
    console.log(recordId);

    $.ajax({
        type: "POST",
        url: "/goals/delete-record",
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



