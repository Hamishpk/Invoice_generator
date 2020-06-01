$(document).ready(function(){
	var table = null;
  $("#invoice button").click(function (ev) {
  ev.preventDefault()
  if ($(this).attr("value") == "save") {
    $.ajax({
      data : {
        client_name : $('#clientName').val(),
			  issue_date : $('#issueDate').val(),
			  due_date : $('#dueDate').val(),
				invoice_id : $('#invoiceId').val(),
      },
      type : 'POST',
      url : '/save_edit_invoice'
    })
		.done(function(data){
			window.location = "/";
		})
  }
  if ($(this).attr("value") == "item") {
		$.ajax({
			data : {
				invoice_id : $('#invoiceId').val(),
				product : $('#productInput').val(),
				quantity : $('#quantityInput').val(),
        price : $('#priceInput').val()
			},
			type : 'POST',
			url : '/process'
		})
    .done(function(data){
      $("#resultsTable").html(data.my_table);
			table = $("#a_nice_table").DataTable();
    })
  }

  });
});
