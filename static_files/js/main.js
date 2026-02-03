// Helper functions (replaces jQuery-dependent functions)
function loderin() {
  const loader = document.getElementById("page-loader");
  if (loader) {
    loader.style.display = "flex";
    loader.classList.remove("hidden");
  }
}
function loderout() {
  const loader = document.getElementById("page-loader");
  if (loader) {
    loader.classList.add("hidden");
    setTimeout(function () {
      loader.style.display = "none";
    }, 500);
  }
}
// Modern loader - only shows on initial page load
document.addEventListener("DOMContentLoaded", function () {
  const pageLoader = document.getElementById("page-loader");

  // Hide loader when page is fully loaded
  window.addEventListener("load", function () {
    setTimeout(function () {
      if (pageLoader) {
        pageLoader.classList.add("hidden");
        // Remove loader from DOM after animation completes
        setTimeout(function () {
          pageLoader.style.display = "none";
        }, 500);
      }
    }, 300);
  });

  // Fallback: Hide loader after maximum 3 seconds even if page doesn't fully load
  setTimeout(function () {
    if (pageLoader && !pageLoader.classList.contains("hidden")) {
      pageLoader.classList.add("hidden");
      setTimeout(function () {
        pageLoader.style.display = "none";
      }, 500);
    }
  }, 3000);
});

const alert_on = (color, text) => {
  console.log(`ads-alert-${color}-text`);
  document.getElementById(`ads-alert-${color}-text`).innerText = text;
  document.getElementById(`ads-alert-${color}`).style.display = "block";
  setTimeout(function () {
    document.getElementById(`ads-alert-${color}`).style.display = "none";
  }, 2000);
};
var tooltipTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="tooltip"]'),
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});
document.addEventListener("DOMContentLoaded", function () {
  const currentPath = window.location.pathname;
  const links = document.querySelectorAll("#mainNavbar a.nav-link[href]");
  links.forEach(function (link) {
    if (link.getAttribute("href") === currentPath) {
      link.classList.add("active");
    }
  });
});
