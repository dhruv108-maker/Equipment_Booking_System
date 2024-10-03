$(document).ready(function(){
    var prevScroll = 0;
    var $window = $(window);
    var $nav = $('#navbar');
    
    $window.on('scroll', function(){
        var currentScroll = $window.scrollTop();
        
        if (currentScroll > prevScroll) {
            // Scrolling Down
            $nav.addClass('hidden');
        } else {
            // Scrolling Up
            $nav.removeClass('hidden');
        }
        
        prevScroll = currentScroll;
    });
});

function openHomePage(){
  window.open('/home', '_blank')
}

function openLoginPgae(){
  window.open('/', '_blank')
}

function openRequetsPgae(){
  window.open('/requests', '_blank')
}

function openInputPage() {
  const equipmentCardContainer = document.getElementById('equipment-card-container');
  const inputFormContainer = document.getElementById('input-form-container');

  // Hide the equipment card and show the input form with smooth transitions
  equipmentCardContainer.style.display = 'none';
  inputFormContainer.style.display = 'flex';
  inputFormContainer.style.justifyContent = 'center';
  inputFormContainer.style.width = '100%';
  
  // Optional: Add smooth transitions by changing opacity
  inputFormContainer.style.opacity = 0;
  setTimeout(() => {
      inputFormContainer.style.transition = 'opacity 0.5s ease';
      inputFormContainer.style.opacity = 1;
  }, 10);  // Delay for ensuring the transition takes effect
}

function openEquipmentPage(){
  window.open('/equipment_information', '_blank')
}

window.onload = function() {
  // Check the current URL
  var currentUrl = window.location.href;

  // If the URL matches http://192.168.29.113:5000/
  if (currentUrl === "http://192.168.29.200:5000/#") {
    // Hide the navbar
    document.getElementById("navBar").style.display = "none";
  }
};