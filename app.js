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

    // category-item
      document.querySelectorAll('.category-item').forEach(item => {
    item.addEventListener('click', function () {
      // Remove active class from all
      document.querySelectorAll('.category-item').forEach(i => i.classList.remove('active'));
      
      // Add active class to clicked item
      this.classList.add('active');
    });
  });

    // vetables.html

  document.addEventListener("DOMContentLoaded", function () {
    // Target all boxes with the class
    document.querySelectorAll(".custom-box").forEach(function (box) {
      box.style.cursor = "pointer";

      box.addEventListener("click", function () {
        const url = box.getAttribute("data-url"); 
        if (url) {
          window.location.href = url; 
        }
      });
    });
  });

  // for google microphone
 
  const micIcon = document.getElementById("micIcon");
  const voicePopup = document.getElementById("voicePopup");

  micIcon.addEventListener("click", () => {
    voicePopup.style.display = "block";
  });

  function closePopup() {
    voicePopup.style.display = "none";
  }

// Example product list (you can replace this with API call later)
const items = [
  "Mango", "Banana", "Apple", "Litchi", "Tomato", "Diaper XXL",
  "Milk", "Bread", "Butter", "Chips", "Chocolates"
];

searchInput.addEventListener("input", () => {
  const query = searchInput.value.toLowerCase();
  if (query.trim() === "") {
    liveResults.style.display = "none";
    return;
  }

  const filtered = items.filter(item => item.toLowerCase().includes(query));
  
  if (filtered.length === 0) {
    liveResults.innerHTML = "<p>No results found</p>";
  } else {
    liveResults.innerHTML = filtered.map(item => `<p>${item}</p>`).join("");
  }

  liveResults.style.display = "block";
});

// Optional: Hide result box when user clicks outside
document.addEventListener("click", function (e) {
  if (!searchInput.contains(e.target) && !liveResults.contains(e.target)) {
    liveResults.style.display = "none";
  }
});





  // oil html

    document.addEventListener("DOMContentLoaded", function () {
    // Target all boxes with the class
    document.querySelectorAll(".flex-week").forEach(function (box) {
      box.style.cursor = "pointer"; 

      box.addEventListener("click", function () {
        const url = box.getAttribute("data-url"); 
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

  // paancontainer

    document.querySelectorAll(".flex").forEach(card => {
    card.addEventListener("click", () => {
      const url = card.getAttribute("data-url");
      if (url) {
        window.location.href = url;
      }
    });
  });

  // for navbar refresh

const categoryItems = document.querySelectorAll(".category-item");
const contentArea = document.getElementById("categoryContent");
const loader = document.getElementById("loader"); 

categoryItems.forEach(item => {
  item.addEventListener("click", () => {
    const category = item.getAttribute("data-category");

    // Scroll to top and show loader
    window.scrollTo({ top: 0, behavior: 'smooth' });
    loader.style.display = "block";
    contentArea.style.display = "none";

    // Fetch data from Flask backend
fetch(`https://blinkit-clone-mywx.onrender.com/api/category/${category}`)
  .then(res => res.json())
  .then(data => {


    let html = `<div class="row g-2">`;  

data.products.forEach(product => {
  html += `
    <div class="col-4">
      <div class="card-pro shadow-sm p-2 align-items-center" style="height: auto;">
        <img src="${product.image}" alt="${product.name}" class="img-fluid rounded" 
             style="width: 400px; height: 180px; object-fit: cover; flex-shrink: 0;">
        <div class="d-flex flex-row m-2" style="width: 100%";>
          <h6 class="mb-1">${product.name}</h6>
          <p class="mb-0 text-muted">₹${product.price}</p>
        </div>
      </div>
    </div>
  `;
});

html += `</div>`;


    contentArea.innerHTML = html;
  })
  .catch(err => {
    contentArea.innerHTML = `<p class="text-danger">Error loading content.</p>`;
    console.error("Fetch error:", err);
  })
  .finally(() => {
    loader.style.display = "none";
    contentArea.style.display = "block";
  });


  });
});



// for footer fix when i navigate
function loadPage(page) {
  const content = document.getElementById("content-area");

  if (page === "home") {
    content.innerHTML = "<h1>Welcome to Home Page</h1>";
  } else if (page === "order") {
    content.innerHTML = "<h1>Order Again Page</h1>";
  } else if (page === "categories") {
    content.innerHTML = "<h1>Categories Page</h1>";
  } else if (page === "print") {
    content.innerHTML = "<h1>Print Page</h1>";
  }
}







