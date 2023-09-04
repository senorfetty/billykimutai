
const t = document.getElementById('navtitle');
document.querySelector('.navbar-toggler').addEventListener ("click", function () {
  t.style.display = this.getAttribute("aria-expanded") === "true" ? "none" : "block" ;
});


const scrollLinks = document.querySelectorAll('.scroll-link');
scrollLinks.forEach(link => {
  link.addEventListener('click', (event) => {
    event.preventDefault(); // Prevent default link behavior
    const targetId = link.getAttribute('href'); // Get the target section's ID
    const targetSection = document.querySelector(targetId); // Find the target section element

    const navbarHeight = document.querySelector('nav').offsetHeight;
    const targetOffset = targetSection.offsetTop - navbarHeight;

    // Scroll smoothly to the target section with offset
    window.scrollTo({
      top: targetOffset,
      behavior: 'smooth'
    });

    // Code to close the toggle navigation
    const navbarToggle = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    navbarCollapse.classList.remove('show');
  });
});


// // Get all skill elements
// const skillElements = document.querySelectorAll('.skill');

// // Add event listener to each skill element
// skillElements.forEach((skillElement) => {
//   skillElement.addEventListener('click', animateProgressBar);
// });

// // Function to animate the progress bar
// function animateProgressBar(event) {
//   // Find the progress bar within the clicked skill element
//   const progressBar = event.currentTarget.querySelector('.progress-bar');

//   // Get the width percentage from the skill-percentage span
//   const skillPercentage = event.currentTarget.querySelector('.skill-percentage').textContent;

//   // Animate the progress bar width
//   progressBar.style.width = skillPercentage;
// }


document.getElementById('cont').addEventListener('submit', async function (e) {
  e.preventDefault();
  const emailInput = document.getElementById('email-input');
  const email = emailInput.value;

  const response = await fetch('/verify_email/', {
      method: 'POST',
      body: JSON.stringify({ email }),
      headers: {
          'Content-Type': 'application/json',
      },
  });

  const data = await response.json();

  if (data.is_valid) {
      // Email is valid, proceed with form submission
      this.submit();
  } else {
      alert('Please enter a valid email address.');
  }
});