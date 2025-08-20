document.addEventListener("DOMContentLoaded", () => {
  // The main container for all device elements
  const elementsContainer = document.querySelector(".containers");

  const formatDuration = (seconds) => {
    if (seconds < 60) return `${Math.floor(seconds)} seconds ago`;
    if (seconds < 3600) return `${Math.floor(seconds / 60)} minutes ago`;
    if (seconds < 86400) return `${Math.floor(seconds / 3600)} hour ago`;
    if (seconds < 172800) return `${Math.floor(seconds / 3600)} hours ago`;
    if (seconds < 2592000) return `${Math.floor(seconds / 86400)} days ago`;
    return `a very long time ago`;
  };

  async function updateStatus() {
    try {
      const response = await fetch("/api/status");
      const statusData = await response.json();

      // Get all existing device elements on the page
      const deviceElements = document.querySelectorAll(".elements");

      // Iterate through each device element
      deviceElements.forEach((deviceElement) => {
        const deviceName = deviceElement.dataset.deviceName;
        console.log(deviceName);
        // Access the array from the JSON data by taking the first word and converting to lowercase
        const status = statusData[deviceName.split(" ")[0].toLowerCase()];
        console.log(status);

        // Find the status light and text elements within this device's container
        const light = deviceElement.querySelector(".status-light");
        const text = deviceElement.querySelector(".status-text");

        // Check if a status for this device was found
        if (status) {
          const lastSeenDelta = status[0]; // The time delta
          const isOnline = status[1]; // The boolean status

          // Remove existing status classes to prevent conflicts
          light.classList.remove("online", "offline", "unknown");

          let lastSeenText = "";

          console.log(lastSeenDelta, isOnline);

          // Apply the new logic to determine the device state
          if (isOnline) {
            light.classList.add("online");
            lastSeenText = "Online";
          } else if (lastSeenDelta < 60 * 60 * 365.25) {
            // Device was seen in the past year
            light.classList.add("offline");
            lastSeenText = `Offline (Last seen ${formatDuration(
              lastSeenDelta
            )})`;
          } else {
            // lastSeenDelta is -1
            light.classList.add("unknown");
            lastSeenText = "Unknown";
          }

          // Update the text and add the tooltip for hover
          text.textContent = lastSeenText;
          deviceElement.title = lastSeenText;
        } else {
          // Handle devices not found in the API response
          light.classList.remove("online", "offline");
          light.classList.add("unknown");
          text.textContent = "Unknown";
          deviceElement.title = "Device status not found in API response.";
        }
      });
    } catch (error) {
      console.error("Failed to fetch device status:", error);
      // You could also add an error state to the elements here
    }
  }

  // Call the function immediately and set an interval to update it
  updateStatus();
  setInterval(updateStatus, 5000);
});
