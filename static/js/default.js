console.log("Great, Run JS to App!")
window.onload = function() {
	// setup the button click
  question('','',1)
	/*document.getElementById("theButton").onclick = function() {};*/
}

function update(name, score, level, nq) {
console.log(name)
console.log(score)
console.log(level)
console.log(nq)
$(".name").html("Hi "+name)
$(".score").html("Score "+score)
$(".level").html("Level "+level)
$(".questions").html("Questions "+nq)
}

function question(name, answer, level, nq) {
	// ajax the JSON to the server
	$.post("question", {"name":name,"answer":answer,"nq":nq,"level":level}, function (data, status) {
      console.log("question receive:");
      console.log("Ajax post status is " + status);
      console.log(data);
      $(".question").html(data)
  });
	// stop link reloading the page
 event.preventDefault();
}
