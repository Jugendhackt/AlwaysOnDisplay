var cardViews = document.getElementById("card-views");

function addCard(title, text, time) {
    cardViews.innerHTML += "<h1>" + x + "</h1>" + "</br>" + y;
}

function truncate(text) {
    if (text.length >= 75)
        text = text.substring(0, 73) + "..";

    var args = text.split(" ");
    while (biggestArgLength(args) > 15) {
        for (var i = args.length - 1; i >= 0; i--) {
            var arg = args[i];
            if (arg.length > 15) {
                var halfLength = parseInt(arg.length / 2, 10);
                args[i] = arg.substring(0, halfLength);
                for (var j = args.length; j >= i + 2; j--)
                    args[j] = args[j - 1];
                args[i + 1] = arg.substring(halfLength, arg.length);
            }
        }
    }
    return args.join(" ");
}

function biggestArgLength(args) {
    var biggestLength = 0;
    for (var i = 0; i < args.length; i++)
        biggestLength = args[i].length > biggestLength ? args[i].length : biggestLength;
    return biggestLength;
}

function updateCards() {
    var request = new XMLHttpRequest();
    request.open("GET", "http://127.0.0.1:5000/sender");
    request.addEventListener('load', function (event) {
        if (request.status < 200 || request.status >= 300)
            console.warn(request.statusText, request.responseText);

        var obj = JSON.parse(request.responseText);
        console.log(obj);
        addCard(obj.title, obj.text);
    });
    request.send();
}

setInterval(updateCards(), 100);