var scrollWindow = function() {
		$(window).scroll(function(){
			var $w = $(this),
					st = $w.scrollTop(),
					navbar = $('.ftco_navbar'),
					sd = $('.js-scroll-wrap');

			if (st > 150) {
				if ( !navbar.hasClass('scrolled') ) {
					navbar.addClass('scrolled');
				}
			}
			if (st < 150) {
				if ( navbar.hasClass('scrolled') ) {
					navbar.removeClass('scrolled sleep');
				}
			}
			if ( st > 350 ) {
				if ( !navbar.hasClass('awake') ) {
					navbar.addClass('awake');
				}

				if(sd.length > 0) {
					sd.addClass('sleep');
				}
			}
			if ( st < 350 ) {
				if ( navbar.hasClass('awake') ) {
					navbar.removeClass('awake');
					navbar.addClass('sleep');
				}
				if(sd.length > 0) {
					sd.removeClass('sleep');
				}
			}
		});
	};
	scrollWindow();



  $( function() {
    $( ".checkin_date" ).datepicker({
		dateFormat: 'dd/mm/yy',
		minDate:0,
        onSelect: function (dateText, inst) {
                var d = $.datepicker.parseDate(inst.settings.dateFormat, dateText);
             d.setDate(d.getDate() + 1);
                $(".checkout_date").val($.datepicker.formatDate(inst.settings.dateFormat, d));
                $(".checkout_date").datepicker("option", "minDate", d);
           },
    });
  } );

   $( function() {
    $( ".checkout_date" ).datepicker({
		dateFormat: 'dd/mm/yy',
        minDate: 0
    });
  } );

