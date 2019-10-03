console.log("Great, Run JS to App!")
window.onload = function() {
	// setup the button click
  question('','',1)
	/*document.getElementById("theButton").onclick = function() {};*/
}

function update(name, score, level) {
console.log(name)
console.log(score)
console.log(level)
}

function question(user, answer, level) {
	// ajax the JSON to the server
	$.post("question", {"level":level}, function (data, status) {
      console.log("question receive:");
      console.log("Ajax post status is " + status);
      console.log(data);
      $(".question").html(data)
  });
	// stop link reloading the page
 event.preventDefault();
}
