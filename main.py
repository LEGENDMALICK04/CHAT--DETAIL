<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LEGEND-MALICK CHAT DETAILS</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f9f9f9;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            border: 1px solid #ccc;
            border-radius: 10px;
            animation: fadeIn 0.5s ease;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            transition: box-shadow 0.3s ease;
        }
        .form-group input:focus {
            outline: none;
            box-shadow: 0 0 5px rgba(81, 203, 238, 0.8);
        }
        .form-group button {
            width: 100%;
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .form-group button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        #results {
            margin-top: 20px;
        }
        .chat-detail {
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s ease;
            cursor: pointer;
        }
        .chat-detail:hover {
            transform: scale(1.02);
        }
        .chat-detail strong {
            color: #333;
            font-size: 14px;
        }
        .chat-detail ul {
            list-style-type: none;
            padding-left: 0;
        }
        .chat-detail li {
            margin: 5px 0;
            padding: 8px;
            background-color: #e9e9e9;
            border-radius: 4px;
        }
        .chat-detail li:nth-child(even) {
            background-color: #dcdcdc;
        }
        .chat-detail.color-1 {
            background-color: #f1f8e9;
        }
        .chat-detail.color-2 {
            background-color: #e3f2fd;
        }
        .chat-detail.color-3 {
            background-color: #ffecb3;
        }
        .chat-detail.color-4 {
            background-color: #ffccbc;
        }
        .chat-detail.color-5 {
            background-color: #f3e5f5;
        }
        .participants {
            display: none;
            margin-top: 10px;
        }
        .participants-toggle {
            display: block;
            color: #4CAF50;
            cursor: pointer;
            margin-top: 10px;
        }
        .chat-detail.collapsed .participants-toggle {
            display: none;
        }
        .chat-detail.collapsed .participants {
            display: block;
        }
        .copy-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            padding: 5px 10px;
            margin-left: 10px;
            font-size: 12px;
            transition: background-color 0.3s ease;
        }
        .copy-btn:hover {
            background-color: #45a049;
        }
        .copied {
            background-color: #2e7d32;
            pointer-events: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Enter Access Token</h1>
        <div class="form-group">
            <label for="access_token">Access Token:</label>
            <input type="text" id="access_token" name="access_token" required>
        </div>
        <div class="form-group">
            <label for="limit">Limit:</label>
            <input type="number" id="limit" name="limit" value="5" min="1">
        </div>
        <div class="form-group">
            <button type="button" onclick="getChatDetails()">Get Chat Details</button>
        </div>
        <div id="results"></div>
    </div>

    <script>
        function getChatDetails() {
            const accessToken = document.getElementById('access_token').value;
            const limit = document.getElementById('limit').value;

            fetch('/UIDdetails', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ access_token: accessToken, limit: parseInt(limit) })
            })
            .then(response => response.json())
            .then(data => {
                const resultsDiv = document.getElementById('results');
                resultsDiv.innerHTML = '';
                const colors = ['color-1', 'color-2', 'color-3', 'color-4', 'color-5'];
                if (data.length > 0) {
                    data.forEach((chat, index) => {
                        const chatDiv = document.createElement('div');
                        chatDiv.className = `chat-detail ${colors[index % colors.length]}`;
                        chatDiv.innerHTML = `
                            <strong>Chat ID:</strong> ${chat.chat_id}<br>
                            <strong>Chat Name:</strong> ${chat.chat_name}
                            <button class="copy-btn" onclick="copyChatDetails('${chat.chat_id}', '${chat.chat_name}', this)">Copy</button><br>
                            <div class="participants-toggle">Click me to see participants</div>
                            <div class="participants">
                                <strong>Participants:</strong>
                                <ul>
                                    ${chat.participants.map(participant => `
                                        <li>${participant.uid}: ${participant.name}
                                            <button class="copy-btn" onclick="copyText('${participant.uid}: ${participant.name}', this)">Copy</button>
                                        </li>`).join('')}
                                </ul>
                            </div>
                        `;
                        chatDiv.addEventListener('click', () => {
                            chatDiv.classList.toggle('collapsed');
                        });
                        resultsDiv.appendChild(chatDiv);
                    });
                } else {
                    resultsDiv.innerHTML = '<p>No chat details found.</p>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }

        function copyText(text, button) {
            const textarea = document.createElement('textarea');
            textarea.value = text;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            showCopied(button);
        }

        function copyChatDetails(chatId, chatName, button) {
            const text = `Chat ID: ${chatId}, Chat Name: ${chatName}`;
            copyText(text, button);
        }

        function showCopied(button) {
            button.textContent = 'Copied!';
            button.classList.add('copied');
            setTimeout(() => {
                button.textContent = 'Copy';
                button.classList.remove('copied');
            }, 2000);
        }
    </script>
</body>
</html>