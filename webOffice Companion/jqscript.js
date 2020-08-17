//The JQuery script for a dynamic UI
	$(document).ready(function() {
		$('#menu').tabs({
			//handling of tabbed menu and attributes from mode buttons
		});
			$('#dmode').click(function() { 
			
				$('#stl').attr('href','https://code.jquery.com/ui/1.12.1/themes/ui-darkness/jquery-ui.css');
				$('body').attr('bgcolor','#1c1b1b');
				$('body').attr('text','white');
		});	//handling the light and dark themes
			$('#lmode').click(function() { 
			
				$('#stl').attr('href','https://code.jquery.com/ui/1.12.1/themes/ui-lightness/jquery-ui.css');
				$('body').attr('bgcolor','white');
				$('body').attr('text','black');
		}); //making the calendar
			$(function() {
				$('#dp').datepicker();
			});
		});