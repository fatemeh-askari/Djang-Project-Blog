(function($) {

	"use strict";

	/* ----------------------------------------------------------- */
	/*  FUNCTION TO STOP LOCAL AND YOUTUBE VIDEOS IN SLIDESHOW
    /* ----------------------------------------------------------- */

	function stop_videos() {
		var video = document.getElementById("video");
		if (video.paused !== true && video.ended !== true) {
			video.pause();
		}
		$('.youtube-video')[0].contentWindow.postMessage('{"event":"command","func":"' + 'pauseVideo' + '","args":""}', '*');
	}

	$(window).on("load", function() {

		/* ----------------------------------------------------------- */
		/*  PAGE PRELOADER
        /* ----------------------------------------------------------- */
		
		var preloader = $('#preloader');
		setTimeout(function() {
			preloader.addClass('preloaded');
		}, 800);

	});

	$(document).ready(function() {

		/* ----------------------------------------------------------- */
		/*  STOP VIDEOS
        /* ----------------------------------------------------------- */

		$('.slideshow nav span').on('click', function () {
			stop_videos();
		});

		/* ----------------------------------------------------------- */
		/*  MOBILE MENU
		/* ----------------------------------------------------------- */

		$('#mobile-nav li').on('click', function () {
			$('#mobile-nav li').removeClass('active');
			$(this).addClass('active');
			$('#desktop-nav li').removeClass('active');
			var index = $(this).index() + 1;
			$('#desktop-nav li:nth-child(' + index + ')').addClass('active');
		});

		/* ----------------------------------------------------------- */
		/*  DESKTPOP MENU
        /* ----------------------------------------------------------- */

		$('#desktop-nav li').on('click', function () {
			$('#desktop-nav li').removeClass('active');
			$(this).addClass('active');
			$('#mobile-nav li').removeClass('active');
			var index = $(this).index() + 1;
			$('#mobile-nav li:nth-child(' + index + ')').addClass('active');
		});

		/* ----------------------------------------------------------- */
		/*  PORTFOLIO GALLERY
        /* ----------------------------------------------------------- */

		if ($('.gridlist').length) {
			new CBPGridGallery( document.getElementById( 'grid-gallery' ) );
		}

		/* ----------------------------------------------------------- */
		/*  HIDE HEADER WHEN PORTFOLIO SLIDESHOW OPENED
        /* ----------------------------------------------------------- */

		$(".gridlist figure").on('click', function() {
			$("#navbar-collapse-toggle").addClass('hide-header');
			if ($(window).width() < 992) {
				$('#menuToggle').addClass('hideMenuToggle');
			}
		});

		/* ----------------------------------------------------------- */
		/*  SHOW HEADER WHEN PORTFOLIO SLIDESHOW CLOSED
        /* ----------------------------------------------------------- */

		$(".nav-close").on('click', function() {
			$("#navbar-collapse-toggle").removeClass('hide-header');
			$('#menuToggle').removeClass('hideMenuToggle');
		});
		$(".nav-prev").on('click', function() {
			if ($('.slideshow ul li:first-child').hasClass('current')) {
				$("#navbar-collapse-toggle").removeClass('hide-header');
				$('#menuToggle').removeClass('hideMenuToggle');
			}
		});
		$(".nav-next").on('click', function() {
			if ($('.slideshow ul li:last-child').hasClass('current')) {
				$("#navbar-collapse-toggle").removeClass('hide-header');
				$('#menuToggle').removeClass('hideMenuToggle');
			}
		});

		/* ----------------------------------------------------------- */
		/*  PORTFOLIO DIRECTION AWARE HOVER EFFECT
        /* ----------------------------------------------------------- */

		var item = $(".gridlist li figure");
		var elementsLength = item.length;
		for (var i = 0; i < elementsLength; i++) {
			if ($(window).width() > 991) {
				$(item[i]).hoverdir();
			}
		}

		/* ----------------------------------------------------------- */
		/*  AJAX CONTACT FORM
        /* ----------------------------------------------------------- */

		// $("#contactform").on("submit", function() {
		// 	$("#message").text("Sending...");
		// 	var form = $(this);
		// 	$.ajax({
		// 		url: form.attr("action"),
		// 		method: form.attr("method"),
		// 		data: form.serialize(),
		// 		success: function(result) {
		// 			if (result === "success") {
		// 				$("#contactform").find(".output_message").addClass("success");
		// 				$("#message").text("Message Sent!");
		// 			} else {
		// 				$("#contactform").find(".output_message").addClass("error");
		// 				$("#message").text("Error Sending!");
		// 			}
		// 		}
		// 	});
		// 	return false;
		// });

	});

	$(document).keyup(function(e) {

		/* ----------------------------------------------------------- */
		/*  KEYBOARD NAVIGATION IN PORTFOLIO SLIDESHOW
        /* ----------------------------------------------------------- */
		if (e.keyCode === 27) {
			stop_videos();
			$('.close-content').click();
			$("#navbar-collapse-toggle").removeClass('hide-header');
		}
		if ((e.keyCode === 37) || (e.keyCode === 39)) {
			stop_videos();
		}
	});


})(jQuery);





// To achieve the functionality where the active page's icon is highlighted in the navigation menu
document.addEventListener("DOMContentLoaded", function() {
    // Get the current path of the URL
    var currentPath = window.location.pathname;

    // Get all the list items in the navigation menu
    var navItems = document.querySelectorAll("#desktop-nav li");

    // Loop through each list item
    navItems.forEach(function(item) {
        // Remove the 'active' class from all list items
        item.classList.remove("active");

        // Get the anchor element inside the list item
        var link = item.querySelector("a");

        // Get the href attribute of the anchor element
        var href = link.getAttribute("href");

        // Check if the current path matches the href attribute
        if (currentPath === href) {
            // Add the 'active' class to the list item
            item.classList.add("active");
        }
    });
});




