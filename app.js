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
     
      document.querySelectorAll('.category-item').forEach(i => i.classList.remove('active'));
      this.classList.add('active');
    });
  });



  // for logo
   setTimeout(() => {
    document.getElementById('splash-screen').style.display = 'none';
    document.getElementById('main-content').style.display = 'block';
  }, 3000);

    // vetables.html

  document.addEventListener("DOMContentLoaded", function () {
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

  // oil html

    document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".flex-week").forEach(function (box) {
      box.style.cursor = "pointer"; 

      box.addEventListener("click", function () {
        const url = box.getAttribute("data-url"); 
        if (url) {
          window.location.href = url;
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








