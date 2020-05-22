$(document).ready(function(){
	console.log('hello')
  $("#invoice button").click(function (ev) {
  ev.preventDefault()
  if ($(this).attr("value") == "save") {
    $.ajax({
      data : {
        client_name : $('#clientName').val(),
			  issue_date : $('#issueDate').val(),
			  due_date : $('#dueDate').val(),
      },
      type : 'POST',
      url : '/add_invoice'
    })
		.done(function(data){
			console.log('invoice added')
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
      console.log('item added')
    })
  }

  });
});
