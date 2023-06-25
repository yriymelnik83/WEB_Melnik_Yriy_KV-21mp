const chatSocket = new WebSocket(
    'ws://'
    + window.location.host 
    + '/ws'
)

chatSocket.onmessage = (e) => {
    const data = JSON.parse(e.data)
    console.log(data.message)
    document.getElementById("chatArea").textContent += data.userName + " : " + data.message + '\n' 
}

chatSocket.onclose = (e) => {
    console.error('Chat socket closed unexpectedly')
}
let messageTextElement = document.getElementById("messageText")
function sendMessage() {
    const message = messageTextElement.value
    const name = messageTextElement.dataset.username ? messageTextElement.dataset.username : "anonymus" 
    chatSocket.send(JSON.stringify({
        'message' : message,
        'userName' : name,
    }))
    messageTextElement.value = ""
}
