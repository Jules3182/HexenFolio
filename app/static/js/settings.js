async function loadThemes() {
  const select = document.getElementById("theme-select");

  const res = await fetch("/api/settings/themes");
  const data = await res.json();

  select.innerHTML = "";

  data.themes.forEach(theme => {
    const option = document.createElement("option");
    option.value = theme;
    option.textContent = theme.charAt(0).toUpperCase() + theme.slice(1);
    select.appendChild(option);
  });

  // Set current theme
  select.value = localStorage.getItem("theme") || data.themes[0];
}

document.addEventListener("DOMContentLoaded", () => {
  loadThemes();

  document.getElementById("theme-select").addEventListener("change", e => {
    setTheme(e.target.value);
  });
});