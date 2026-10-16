:root {
    --bg-primary: #0b0f19;
    --card-bg: #111827;
    --card-border: #1f2937;
    --text-primary: #f9fafb;
    --text-secondary: #9ca3af;
    --accent-primary: #6366f1;
    --accent-hover: #4f46e5;
    --input-bg: #1f2937;
    --chat-user-bg: #4f46e5;
    --chat-ai-bg: #1f2937;
}

[data-theme="light"] {
    --bg-primary: #f3f4f6;
    --card-bg: #ffffff;
    --card-border: #e5e7eb;
    --text-primary: #111827;
    --text-secondary: #4b5563;
    --accent-primary: #4f46e5;
    --accent-hover: #4338ca;
    --input-bg: #f9fafb;
    --chat-user-bg: #6366f1;
    --chat-ai-bg: #e5e7eb;
}

body {
    margin: 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--bg-primary);
    color: var(--text-primary);
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 30px;
    background: var(--card-bg);
    border-bottom: 1px solid var(--card-border);
}

.brand { display: flex; align-items: center; gap: 15px; }
.brand-icon { font-size: 2rem; }
.brand h1 { margin: 0; font-size: 1.3rem; }
.brand p { margin: 0; font-size: 0.8rem; color: var(--text-secondary); }

.theme-toggle-btn {
    background: var(--input-bg);
    border: 1px solid var(--card-border);
    color: var(--text-primary);
    padding: 8px 16px;
    border-radius: 8px;
    cursor: pointer;
}

.tab-navigation {
    display: flex;
    justify-content: center;
    gap: 10px;
    padding: 15px;
    background: var(--card-bg);
    border-bottom: 1px solid var(--card-border);
}

.tab-btn {
    background: transparent;
    border: none;
    color: var(--text-secondary);
    padding: 10px 20px;
    font-weight: 600;
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.tab-btn.active, .tab-btn:hover {
    background: var(--accent-primary);
    color: white;
}

.dashboard-single {
    max-width: 900px;
    margin: 30px auto;
    width: 90%;
    flex: 1;
}

.tab-content { display: none; }
.tab-content.active { display: block; }

.card {
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 12px;
    padding: 25px;
}

.card-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
}

.card-header h2 { margin: 0; font-size: 1.2rem; }

.form-group { margin-bottom: 15px; }
.form-group label { display: block; margin-bottom: 5px; font-size: 0.85rem; color: var(--text-secondary); }

.form-control {
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    border: 1px solid var(--card-border);
    background: var(--input-bg);
    color: var(--text-primary);
    box-sizing: border-box;
}

.btn-submit {
    width: 100%;
    padding: 12px;
    background: var(--accent-primary);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    margin-top: 10px;
}

.btn-submit:hover { background: var(--accent-hover); }

.prediction-card {
    margin-top: 20px;
    background: var(--input-bg);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    border: 1px solid var(--card-border);
}

.price-display {
    font-size: 2rem;
    font-weight: bold;
    color: #10b981;
    margin: 10px 0;
}

.chat-container {
    display: flex;
    flex-direction: column;
    height: 400px;
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.msg {
    max-width: 80%;
    padding: 10px 15px;
    border-radius: 10px;
    font-size: 0.9rem;
    line-height: 1.4;
}

.msg.user {
    align-self: flex-end;
    background: var(--chat-user-bg);
    color: white;
}

.msg.ai {
    align-self: flex-start;
    background: var(--chat-ai-bg);
    color: var(--text-primary);
    border: 1px solid var(--card-border);
}

.chat-input-bar {
    display: flex;
    gap: 10px;
    margin-top: 10px;
}

footer {
    text-align: center;
    padding: 15px;
    font-size: 0.8rem;
    color: var(--text-secondary);
    border-top: 1px solid var(--card-border);
    background: var(--card-bg);
}