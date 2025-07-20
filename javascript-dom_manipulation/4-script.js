document.addEventListener('DOMContentLoaded', function() {
    const addItem = document.getElementById('add_item');
    addItem.addEventListener('click', function() {
      const myList = document.querySelector('ul.my_list');
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      myList.appendChild(newItem);
    });
  }); 
