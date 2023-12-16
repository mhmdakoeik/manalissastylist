    // Function to open the overlay with clicked image
    function openOverlay(imgId) {
        var imgSrc = document.getElementById(imgId).src;
        document.getElementById('expandedImg').src = imgSrc;
        document.getElementById('overlay').style.display = 'flex';
    }

    // Function to close the overlay
    function closeOverlay() {
        document.getElementById('overlay').style.display = 'none';
    }

    // Add click event listeners to each image
    var images = document.querySelectorAll('.cont img');
    images.forEach(function(img) {
        img.addEventListener('click', function() {
            openOverlay(this.id);
        });
    });