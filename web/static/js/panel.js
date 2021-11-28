$(function(){
	$nav = $('.panel');
	$nav.css('width', $nav.outerWidth());
	$window = $(window);
	$h = $nav.offset().top;
	$window.scroll(function(){
		if ($window.scrollTop() > $h) {
			$nav.addClass('fixed');
		} else {
			$nav.removeClass('fixed');
		}
	});
});

