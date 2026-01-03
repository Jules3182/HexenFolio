function cssVar(name) {
  return getComputedStyle(document.documentElement)
    .getPropertyValue(name)
    .trim();
}

let chartInitialized = false;

async function loadPortfolioHistory() {
  console.log("loadPortfolioHistory called");
  const res = await fetch("/api/history");
  if (!res.ok) return;

  const history = await res.json();
  if (history.length === 0) {
  Plotly.newPlot("portfolio-line", [], {
    paper_bgcolor: cssVar("--bg"),
    plot_bgcolor: cssVar("--bg"),
    annotations: [{
      text: "Waiting for market data…",
      xref: "paper",
      yref: "paper",
      showarrow: false,
      font: { size: 16, color: cssVar("--text") }
    }]
  });
  return;
}

  const x = history.map(p => new Date(p.timestamp));
  const y = history.map(p => p.total_value);

  const isUp =
    y[y.length - 1] >= y[0];

  const trace = {
    x,
    y,
    type: "scatter",
    mode: "lines+markers",
    marker: {
        size: y.map((_, i) => i === y.length - 1 ? 10 : 0)
  },
  line: {
      width: 3,
      shape: "spline",
      color: isUp ? cssVar("--up") : cssVar("--down")
    }
  };

  const layout = {
    title: "Total Portfolio Value",
    paper_bgcolor: cssVar("--bg"),
    plot_bgcolor: cssVar("--bg"),
    width: window.innerWidth * 1.05,
    height: 400,
    font: {
      color: cssVar("--text")
    },
    yaxis: {
      title: "",
      tickprefix: "$",
      gridcolor: cssVar("--border")
    },
    xaxis: {
      title: "",
      gridcolor: cssVar("--border")
    },
    margin: { t: 50 }
  };

  if (!chartInitialized) {
    Plotly.newPlot("portfolio-line", [trace], layout, {
      displayModeBar: false,
      responsive: true,
      transition: {
        duration: 500,
        easing: "cubic-in-out"
      }
    });
    chartInitialized = true;
  } else {
    Plotly.react("portfolio-line", [trace], layout);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  loadPortfolioHistory();
  setInterval(loadPortfolioHistory, 1_000);
});