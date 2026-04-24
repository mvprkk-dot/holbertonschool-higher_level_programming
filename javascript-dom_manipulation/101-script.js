document.addEventListener('DOMContentLoaded', () => {
  const translateBtn = document.querySelector('#btn_translate');
  const languageSelect = document.querySelector('#language_code');
  const helloDiv = document.querySelector('#hello');

  translateBtn.addEventListener('click', () => {
    const langCode = languageSelect.value;
    
    // Only proceed if a language is selected
    if (langCode) {
      const url = `https://hellosalut.stefanbohacek.com/?lang=${langCode}`;
      
      fetch(url)
        .then((response) => response.json())
        .then((data) => {
          helloDiv.textContent = data.hello;
        })
        .catch((error) => {
          console.error('Error fetching translation:', error);
        });
    }
  });
});
