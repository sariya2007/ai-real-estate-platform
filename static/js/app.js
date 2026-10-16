function showTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
    
    document.getElementById(tabId).classList.add('active');
    event.target.classList.add('active');
}

async function handlePredict(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const res = await fetch('/predict', { method: 'POST', body: formData });
    const data = await res.json();
    
    const resDiv = document.getElementById('pred-result');
    resDiv.classList.remove('hidden');
    resDiv.innerHTML = `<strong>Estimated Value:</strong> ${data.formatted_price}`;
}

async function handleRecommend(e) {
    e.preventDefault();
    const formData = new FormData(e.target);
    const res = await fetch('/recommend', { method: 'POST', body: formData });
    const data = await res.json();
    
    const container = document.getElementById('rec-results');
    container.innerHTML = '<h3>Recommended Properties:</h3>';
    
    if(!data.recommendations || data.recommendations.length === 0) {
        container.innerHTML += '<p>No matching properties found.</p>';
        return;
    }

    data.recommendations.forEach(item => {
        container.innerHTML += `
            <div style="border:1px solid #e2e8f0; padding:10px; margin-top:10px; border-radius:5px;">
                <h4>Property ID #${item.id} - ${item.location}</h4>
                <p><strong>Price:</strong> ${item.price_pkr} | <strong>Area:</strong> ${item.area_sqft} sqft | <strong>Beds:</strong> ${item.bedrooms}</p>
                <p><em>${item.reason}</em></p>
            </div>
        `;
    });
}

async function handleChat(e) {
    e.preventDefault();
    const input = document.getElementById('chat-input');
    const useRag = document.getElementById('use-rag').checked;
    const chatBox = document.getElementById('chat-box');
    
    const query = input.value;
    chatBox.innerHTML += `<div class="chat-msg user"><strong>You:</strong> ${query}</div>`;
    input.value = '';
    
    const formData = new FormData();
    formData.append('query', query);
    formData.append('use_rag', useRag);

    const res = await fetch('/chat', { method: 'POST', body: formData });
    const data = await res.json();
    
    chatBox.innerHTML += `<div class="chat-msg bot"><strong>AI:</strong> ${data.answer}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}