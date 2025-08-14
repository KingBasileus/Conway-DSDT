function redirectToYouTube() {
    var messageContainer = document.getElementById("message-container");
    messageContainer.innerHTML = "<h2>Maybe you actually ran this :) <3 Christian </h2>";


    setTimeout(function () {
        window.location.href = "https://www.youtube.com/watch?v=Aq5WXmQQooo";
    }, 4000);
}


