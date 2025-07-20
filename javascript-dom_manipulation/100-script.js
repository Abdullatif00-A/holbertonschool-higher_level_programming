document.addEventListener('DOMContentLoaded', function() {
    const addItemButton = document.getElementById('add_item');
    const removeItemButton = document.getElementById('remove_item');
    const clearListButton = document.getElementById('clear_list');
    const list = document.querySelector('.my_list');
  
    addItemButton.addEventListener('click', function() {
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      list.appendChild(newItem);
    });
  
    removeItemButton.addEventListener('click', function() {
      if (list.lastChild) {
        list.removeChild(list.lastChild);
      }
    });
  
    clearListButton.addEventListener('click', function() {
      while (list.firstChild) {
        list.removeChild(list.firstChild);
      }
    });
  }); 
