let header = $("header")
$("#toggle_header").on("click", () => {
	if (header.hasClass("red") && (header.hasClass("green")))
		header.removeClass("green")
	if (header.hasClass("red") === false && header.hasClass("green") === false)
		header.addClass("red")
	header.hasClass("red") ? header.css("color", "green") : header.css("color", "red")
})
