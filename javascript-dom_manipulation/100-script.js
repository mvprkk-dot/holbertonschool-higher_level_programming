document.addEventListener('DOMContentLoaded', () => {
  const addBtn = document.querySelector('#add_item');
  const removeBtn = document.querySelector('#remove_item');
  const clearBtn = document.querySelector('#clear_list');
  const myList = document.querySelector('.my_list');

  // Add a new <li>Item</li>
  addBtn.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  // Remove the last <li> element
  removeBtn.addEventListener('click', () => {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      myList.removeChild(lastItem);
    }
  });

  // Remove all <li> elements
  clearBtn.addEventListener('click', () => {
    myList.innerHTML = '';
  });
});
