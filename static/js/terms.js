    document.getElementById('agreeCheck').addEventListener('change', function () {
      document.getElementById('acceptBtn').disabled = !this.checked;
    });
  
    document.getElementById('acceptBtn').addEventListener('click', function () {
      if (document.getElementById('agreeCheck').checked) {
        window.location.href = 'https://calendly.com/30minfree-consultation-call/30min';
      }
    });
