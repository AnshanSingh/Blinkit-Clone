      fetch('navbar.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('navbar-placeholder').innerHTML = data;
    });

      fetch("footer.html")
    .then(res => res.text())
    .then(data => {
      document.getElementById("footer-placeholder").innerHTML = data;
    });

    // vetables.html

  document.addEventListener("DOMContentLoaded", function () {
    // Target all boxes with the class
    document.querySelectorAll(".custom-box").forEach(function (box) {
      box.style.cursor = "pointer"; // change cursor to pointer

      box.addEventListener("click", function () {
        const url = box.getAttribute("data-url"); // e.g., "vegetables.html"
        if (url) {
          window.location.href = url; // redirect
        }
      });
    });
  });


  // oil html

    document.addEventListener("DOMContentLoaded", function () {
    // Target all boxes with the class
    document.querySelectorAll(".flex-week").forEach(function (box) {
      box.style.cursor = "pointer"; // change cursor to pointer

      box.addEventListener("click", function () {
        const url = box.getAttribute("data-url"); // e.g., "vegetables.html"
        if (url) {
          window.location.href = url; // redirect
        }
      });
    });
  });

  // sticky navbar

   window.addEventListener("scroll", function () {
    const stickyElement = document.getElementById("stickyElement");
    const stickyOffset = stickyElement.offsetTop;

    if (window.scrollY > stickyOffset) {
      stickyElement.classList.add("fixed");
    } else {
      stickyElement.classList.remove("fixed");
    }
  });


