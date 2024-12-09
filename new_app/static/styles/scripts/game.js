async function submitAnswer(answer) {
    try {
        // Send answer to the backend
        const response = await fetch('/answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ answer: answer })
        });

        if (!response.ok) {
            throw new Error('Failed to submit answer');
        }

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            window.location.href = '/';
            return;
        }

        // Update score
        document.querySelector('.score').innerText = `Score: ${data.score}`;

        if (data.next_question) {
            // Update question and image
            document.querySelector('.question').innerText = data.next_question.question;
            document.querySelector('.barakoni-image').src = data.next_question.image;

            // Update options
            const optionsContainer = document.querySelector('.options');
            optionsContainer.innerHTML = '';
            data.next_question.options.forEach(option => {
                const button = document.createElement('button');
                button.className = 'option';
                button.innerText = option;
                button.onclick = () => submitAnswer(option);
                optionsContainer.appendChild(button);
            });
        } else {
            alert(`Game Over! Your final score: ${data.score}`);
            window.location.href = '/';
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
}
