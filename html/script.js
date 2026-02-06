let enhancedImageBlob = null;
let originalImageBlob = null;
let comparisonMode = false;

async function enhance() {
  let fileInput = document.getElementById("upload");
  let file = fileInput.files[0];
  
  if (!file) {
    alert("Please select an image first!");
    return;
  }

  // Store original image
  let reader = new FileReader();
  reader.onload = e => originalImageBlob = e.target.result;
  reader.readAsDataURL(file);

  let formData = new FormData();
  formData.append("image", file);

  try {
    let response = await fetch("/enhance", { 
      method: "POST", 
      body: formData 
    });
    
    if (!response.ok) {
      alert("Error enhancing image");
      return;
    }

    enhancedImageBlob = await response.blob();
    let url = URL.createObjectURL(enhancedImageBlob);
    
    document.getElementById("result").src = url;
    document.getElementById("downloadBtn").style.display = "inline-block";
    document.getElementById("compareBtn").style.display = "inline-block";
    
    alert("Image enhanced successfully!");
  } catch (error) {
    alert("Error: " + error.message);
  }
}

function toggleComparison(btn) {
  comparisonMode = !comparisonMode;
  
  let singleView = document.getElementById("singleView");
  let comparisonView = document.getElementById("comparisonView");
  
  if (comparisonMode) {
    singleView.style.display = "none";
    comparisonView.style.display = "block";
    btn.textContent = "Hide Comparison";
    
    setTimeout(() => {
      document.getElementById("originalImg").src = originalImageBlob;
      document.getElementById("enhancedImg").src = URL.createObjectURL(enhancedImageBlob);
      // Trigger initial update to position divider correctly
      updateComparison();
    }, 50);
  } else {
    singleView.style.display = "block";
    comparisonView.style.display = "none";
    btn.textContent = "Show Comparison";
  }
}

// Handle dragging the divider
document.addEventListener('DOMContentLoaded', function() {
  let slider = document.getElementById("slider");
  let container = document.querySelector(".comparison-container");
  let isDragging = false;

  function handleMove(e) {
    if (!isDragging || !container) return;
    
    let rect = container.getBoundingClientRect();
    let x = e.clientX - rect.left;
    let percentage = Math.max(0, Math.min(100, (x / rect.width) * 100));
    
    slider.value = percentage;
    updateComparison();
  }

  function handleMouseDown() {
    isDragging = true;
  }

  function handleMouseUp() {
    isDragging = false;
  }

  slider.addEventListener('mousedown', handleMouseDown);
  document.addEventListener('mousemove', handleMove);
  document.addEventListener('mouseup', handleMouseUp);
});

function updateComparison() {
  let slider = document.getElementById("slider");
  let container = document.querySelector(".comparison-container");
  let originalSide = document.querySelector(".original-side");
  let enhancedSide = document.querySelector(".enhanced-side");
  let divider = document.querySelector(".comparison-divider");
  
  if (slider && container) {
    let value = slider.value;
    let ratio = value / 100;
    
    // Calculate widths based on slider position
    let containerWidth = container.offsetWidth;
    let dividerWidth = divider.offsetWidth;
    let availableWidth = containerWidth - dividerWidth;
    
    // Update side widths
    let originalWidth = Math.floor(availableWidth * ratio);
    let enhancedWidth = Math.floor(availableWidth * (1 - ratio));
    
    originalSide.style.flex = `0 0 ${originalWidth}px`;
    enhancedSide.style.flex = `0 0 ${enhancedWidth}px`;
  }
}

function downloadImage() {
  if (!enhancedImageBlob) {
    alert("No image to download!");
    return;
  }

  let url = URL.createObjectURL(enhancedImageBlob);
  let link = document.createElement("a");
  link.href = url;
  link.download = "enhanced-image.png";
  link.click();
  URL.revokeObjectURL(url);
}