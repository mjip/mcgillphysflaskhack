var numParticles = 1; 
var p1x = 0; // these are for the particles 1, 2, 3's x, y, and q values
var p1y = 0;
var p1q = 0;
var p2x = 0;
var p2y = 0;
var p2q = 0;
var p3x = 0;
var p3y = 0;
var p3q = 0;
var sch = "viridis"; // this is the colour scheme for matplotlib
var flag = 0; // this is set to 1 when a neutral particle gets added to the origin
var counter = 0;

$(document).ready(function(){
	var slider1 = document.getElementById("charge1");
	var output1 = document.getElementById("q1");
	output1.innerHTML = slider1.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider1.oninput = function() {
	    output1.innerHTML = this.value;
	    p1q = this.value;
	    flag = 0;
	    
	} 

	var slider2 = document.getElementById("z1");
	var output2 = document.getElementById("zp1");
	output2.innerHTML = slider2.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider2.oninput = function() {
	    output2.innerHTML = this.value;
	    p1x = this.value;
	    flag = 0;
	    
	} 
	var slider3 = document.getElementById("charge2");
	var output3 = document.getElementById("q2");
	output3.innerHTML = slider3.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider3.oninput = function() {
	    output3.innerHTML = this.value;
	    p1y = this.value;
	    flag = 0;
	    update();
	} 

	var slider4 = document.getElementById("z2");
	var output4 = document.getElementById("zp2");
	output4.innerHTML = slider4.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider4.oninput = function() {
	    output4.innerHTML = this.value;
	    p2q = this.value;
	    flag = 0;
	    
	} 
	var slider5 = document.getElementById("charge3");
	var output5 = document.getElementById("q3");
	output5.innerHTML = slider5.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider5.oninput = function() {
	    output5.innerHTML = this.value;
	    p2x = this.value;
	    flag = 0;
	   
	} 

	var slider6 = document.getElementById("z3");
	var output6 = document.getElementById("zp3");
	output6.innerHTML = slider6.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider6.oninput = function() {
	    output6.innerHTML = this.value;
	    p2y = this.value;
	    flag = 0;
	  
	} 
	var slider7 = document.getElementById("z7");
	var output7 = document.getElementById("zp7");
	output7.innerHTML = slider7.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider7.oninput = function() {
	    output7.innerHTML = this.value;
	    p3q = this.value;
	    flag = 0;
	  
	} 

	var slider8 = document.getElementById("z8");
	var output8 = document.getElementById("zp8");
	output8.innerHTML = slider8.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider8.oninput = function() {
	    output8.innerHTML = this.value;
	    p3x = this.value;
	    flag = 0;
	 
	} 
	var slider9 = document.getElementById("z9");
	var output9 = document.getElementById("zp9");
	output9.innerHTML = slider9.value; // Display the default slider value

	// Update the current slider value (each time you drag the slider handle)
	slider9.oninput = function() {
	    output9.innerHTML = this.value;
	    p3y = this.value;
	    flag = 0;
	   
	} 


});

function uponAddParticle(){
	numParticles++;
	if (numParticles == 2){
		document.getElementById('slidecontainer2').style.visibility = 'visible';
		flag = 1;
	}
	if (numParticles == 3){
		document.getElementById('slidecontainer3').style.visibility = 'visible';
		flag = 1;
	}
	else {
		return;
	}

}

function uponClear(){
	document.getElementById('charge1').value = 0;
	document.getElementById("q1").innerHTML = 0;
	document.getElementById('z1').value = 0;
	document.getElementById("zp1").innerHTML = 0;
	document.getElementById('charge2').value = 0;
	document.getElementById("zp7").innerHTML = 0;
	document.getElementById('z2').value = 0;
	document.getElementById('charge3').value = 0;
	document.getElementById('z3').value = 0;
	document.getElementById('z7').value = 0;
	document.getElementById('z8').value = 0;
	document.getElementById('z9').value = 0;
	
	numParticles = 1;
	document.getElementById('slidecontainer2').style.visibility = 'hidden';
	document.getElementById('slidecontainer3').style.visibility = 'hidden';
}

function updateScheme(){
	sch = document.getElementById('colours').value;
	update();
}

function update(){
	counter++;
	$.ajax({
	    url: "/load_data",
	    type: "post",
	    contentType: "application/json; charset=utf-8",
	    dataType: "json",
	    data: JSON.stringify({'x1' : p1x, 'y1' : p1y, 'q1' : p1q, 'x2' : p2x, 'y2' : p2y, 'q2' : p2q, 'x3' : p3x, 'y3' : p3y, 'q3' : p3q, 'scheme' : sch, 'fl' : flag, 'counter': counter }),
	    success: function(data) {
	    	console.log(data);
	        document.getElementById("myImage").src = "../v"+ counter + ".png";
	    },
	    error: function(error) {
	        console.log(error);
	    }
	});
}