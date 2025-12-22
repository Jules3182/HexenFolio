async function fetchPortfolio() {
    try {
        const res = await fetch("/api/portfolio");
        if (!res.ok) throw new Error("Network response was not OK");
        const data = await res.json();
        return data;
    } catch (err) {
        console.error("Failed to fetch portfolio:", err);
        return null;
    }
}

function renderPortfolio(portfolio) {
    const container = document.getElementById("portfolio-container");

    if (!portfolio) {
        container.innerHTML = "<p>Error loading portfolio</p>";
        return;
    }

    // Simple render (JSON dump for now)
    container.innerHTML = `<pre>${JSON.stringify(portfolio, null, 2)}</pre>`;
}

// Initial render
async function updateLoop() {
    while (true) {
        const portfolio = await fetchPortfolio();
        renderPortfolio(portfolio);

        // Refreshes
        await new Promise(resolve => setTimeout(resolve, 1000));
    }
}

updateLoop();