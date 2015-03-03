var textResponses = ['SMS Sent.'];

var roboReponses = ['Picked Up Call', 'Refused Call', 'Missed Call', 'Wrong Number', 'Number Does Not Exist'];

var followupResponses = ['Negative Sentiment', 'Positive Sentiment', 'Neutral Sentiment', 'Extremely Negative Sentiment', 'Extremely Positive Sentiment'];

function replyText(dom) { 
    var response = textResponses[0];
    var para = document.createElement("p");
    var node = document.createTextNode(response);
    para.appendChild(node);
    var child = document.getElementById(dom);
    child.parentNode.replaceChild(para, child);
}

function replyRobo(dom) { 
    var index = Math.floor((Math.random() * roboReponses.length));
    var response = roboReponses[index];
    var para = document.createElement("p");
    var node = document.createTextNode(response);
    para.appendChild(node);
    var child = document.getElementById(dom);
    child.parentNode.replaceChild(para, child);
}

function replyFollowup(dom) { 
    var index = Math.floor((Math.random() * followupResponses.length));
    var response = followupResponses[index];
    var para = document.createElement("p");
    var node = document.createTextNode(response);
    para.appendChild(node);
    var child = document.getElementById(dom);
    child.parentNode.replaceChild(para, child);
}