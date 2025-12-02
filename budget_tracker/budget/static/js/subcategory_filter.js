document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.getElementById('id_category');
    const subcategorySelect = document.getElementById('id_subcategory');
    
    if (!categorySelect || !subcategorySelect) {
        console.error("Missing elements or data!");
        return;
    }
    
    const subcategories = window.categoriesData;
    if (!subcategories) {
        console.error("Missing categoriesData!");
        return;
    }
    
    function filterSubcategories() {
        const currentSubcategoryValue = subcategorySelect.value;
        console.log(categorySelect.value, subcategorySelect.value);

        const categoryValue = categorySelect.value;
        subcategorySelect.innerHTML = '<option value="">---------</option>';
        
        if (categoryValue && subcategories[categoryValue]) {
            subcategories[categoryValue].forEach(function(subcat) {
                const option = new Option(subcat.name, subcat.id);
                subcategorySelect.appendChild(option);
            });
        }

        if (currentSubcategoryValue && subcategorySelect.querySelector(`option[value="${currentSubcategoryValue}"]`)) {
            subcategorySelect.value = currentSubcategoryValue;
        }
    }
    
    categorySelect.addEventListener('change', filterSubcategories);
    filterSubcategories();
});
