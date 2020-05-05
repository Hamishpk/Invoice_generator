$(document).ready(function() {

	$('form').on('submit', function(event) {
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
		.done(function(data) {

			$('#successAlert').text('Item Added').show();
			$('#successAlert').hide();

		});

		event.preventDefault();

	});

});
