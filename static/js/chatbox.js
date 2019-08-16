$(document).ready(function(){
	$(".chat-text textarea").keypress(function(){
		if(event.which == 13){
			console.log($(".chat-text textarea").val());
			var newChat = $(".chat-text textarea").val();
			$(".msg-insert").append($("<div></div>").text(newChat));
			$(".msg-insert div").addClass("msg-send");
			$(".chat-text textarea").val("");
		}
	})
})