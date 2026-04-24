document.getElementById('toggle_header').addEventListener('click', () => {
    const header = document.querySelector('header');
    if (header.classList.contains('green')) {
      header.classList.remove('green');
      header.classList.add('red');
    } else {
      header.classList.remove('red');
      header.classList.add('green');
