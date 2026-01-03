const TICKER_REFRESH_MS = 30000;

let initialized = false;

async function fetchTickerData() {
  const res = await fetch("/api/ticker");
  if (!res.ok) return null;
  return res.json();
}

function buildContent(lines) {
  return lines.map(line => `
    <span class="ticker-item ${line.trend}">
      ${line.text}
    </span>
  `).join("");
}

function restartAnimation(track) {
  track.style.animation = "none";
  track.offsetHeight; // force reflow
  track.style.animation = null;
}

function forceReflow(el) {
  el.style.display = "none";
  el.offsetHeight; // force layout
  el.style.display = "";
}

async function updateTicker() {
  const res = await fetch("/api/ticker");
  if (!res.ok) return;

  const data = await res.json();
  const track = document.getElementById("ticker-track");
  if (!track || !data.lines?.length) return;

  const content = data.lines.map(line => `
    <span class="ticker-item ${line.trend}">
      ${line.text}
    </span>
  `).join("");

  track.innerHTML = content + content;

  // Safari fix
  forceReflow(track);

  // Restart animation cleanly
  track.style.animation = "none";
  track.offsetHeight;
  track.style.animation = "";
}

// Initial build
updateTicker();

// Refresh periodically 
setInterval(updateTicker, TICKER_REFRESH_MS);