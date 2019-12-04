$(document).ready(function() {
    $( "#open" ).click(function() {
        open();
    });
    $( "#close" ).click(function() {
        close();
    });
});

function open() {
    console.log($('.status').text());
    $('.status').text("Opening...");
    $.ajax({
        url : "/open",
        success : function(data) {
            $('.status').text("Open");
            // auto();
        },
        fail: function(xhr, errorThrown){
            alert('request failed');
            $('.status').html("Failed");
        }
    });
}


function close() {
    $('.status').text("Closing...");
    $.ajax({
        url : "/close",
        success : function(data) {
            $('.status').text("Close");
        },
        fail: function(xhr, errorThrown){
            alert('request failed');
            $('.status').html("Failed");
            // auto();
        }
    });
}

function auto() {
    $.ajax({
        url : "/auto",
        success : function(data) {
            
        },
        fail: function(xhr, errorThrown){
            alert('auto failed');
        }
    });
}
