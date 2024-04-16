const panels = document.querySelectorAll('.panel');
let currentIndex = 0;

function toggleActivePanel() {
    removeActiveClasses();
    panels[currentIndex].classList.add('active');
    currentIndex = (currentIndex + 1) % panels.length;
}

function removeActiveClasses() {
    panels.forEach(panel => {
        panel.classList.remove('active');
    });
}

// Set an interval to automatically toggle active panel
const intervalId = setInterval(toggleActivePanel, 2000); // Change 2000 to the desired interval in milliseconds

// Optionally, you can stop the interval after a certain period
// setTimeout(() => {
//     clearInterval(intervalId);
// }, 10000);
