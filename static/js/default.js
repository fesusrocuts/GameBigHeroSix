console.log("Great, Run JS to App!")
window.onload = function() {
	// setup the button click
  question()
	/*document.getElementById("theButton").onclick = function() {};*/
}

function question() {
	// ajax the JSON to the server
	$.post("question", {"level":1}, function (data, status) {
      console.log("question receive:");
      console.log("Ajax post status is " + status);
      console.log(data);
      $(".question").html(data)
  });
	// stop link reloading the page
 event.preventDefault();
}
