let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 9.3418808, lng: -79.9103851 },
    zoom: 8,
  });
}

initMap();