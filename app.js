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

  // grocery and kitchen
  // masala.html

  document.addEventListener("DOMContentLoaded", function (){
    document.querySelectorAll(".custom-box").forEach(function(box) {
      box.style.cursor = "pointer";

      box.addEventListener("click", function (){
        const url = box.getAttribute("data-url");
        if(url){
          window.location.href = url;
        }
      })
    })
  })

  // for navbar refresh

  const categoryItems = document.querySelectorAll(".category-item");
  const contentArea = document.getElementById("categoryContent");

  categoryItems.forEach(item => {
    item.addEventListener("click", () => {
      const category = item.getAttribute("data-category");

      // Optional loading indicator
      contentArea.innerHTML = "<p>Loading...</p>";

      // Load content from external HTML file
      fetch(`${category}.html`)
        .then(res => {
          if (!res.ok) throw new Error("File not found");
          return res.text();
        })
        .then(html => {
          contentArea.innerHTML = html;
        })
        .catch(err => {
          contentArea.innerHTML = `<p class="text-danger">Content not available.</p>`;
          console.error(err);
        });
    });
  });




